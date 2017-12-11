from xml.etree.ElementTree import *
import profile
import requests
import random
import threading
import time
from System import *


Aree = []
total_robot = 0
numb_aree = 0
starting_number_robot = 0
starting_number_cluster = 0
num_cluster = []

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        invio_thread(self.name, self.counter)
        print("Exiting " + self.name)


# Creazione oggetti in modo strettamente tipico
def tipico():
    global numb_aree, starting_number_cluster, starting_number_robot
    total_cluster_tipoco = 100
    total_robot_per_cluster_tipico = 900
    Aree.append(Area(numb_aree))
    Aree[numb_aree].set_cluster(total_cluster_tipoco, starting_number_cluster)
    for c in range(len(Aree[numb_aree].Cluster)):
        starting_number_robot = Aree[numb_aree].Cluster[c].set_robot(total_robot_per_cluster_tipico,
                                                                     starting_number_robot)


# Creazione oggetti in modo custum randomico
def tipico_randomico():
    global numb_aree, starting_number_robot, starting_number_cluster, total_robot, num_cluster
    while total_robot < 90000:
        if total_robot < 50000:
            numb_of_cluster = random.randint(20, 50)
            Aree.append(Area(numb_aree))
            starting_number_cluster = Aree[numb_aree].set_cluster(numb_of_cluster, starting_number_cluster)
            for c in range(numb_of_cluster):
                numb_of_robot = random.randint(500, 1000)
                starting_number_robot = Aree[numb_aree].Cluster[c].set_robot(numb_of_robot, starting_number_robot)
                # print('Area:', numb_aree, ' Cluster: ', c, ' Robot : ', numb_of_robot)
                total_robot = total_robot + numb_of_robot
            num_cluster.append(numb_of_cluster - 1)
            numb_aree = numb_aree + 1
        else:
            numb_remainder = 90000 - total_robot
            max_numb_of_cluster_remainder = int(numb_remainder / 600)
            min_numb_of_cluster_remainder = int(numb_remainder / 900)
            numb_of_cluster = random.randint(min_numb_of_cluster_remainder, max_numb_of_cluster_remainder)
            Aree.append(Area(numb_aree))
            num_cluster.append(numb_of_cluster - 1)
            starting_number_cluster = Aree[numb_aree].set_cluster(numb_of_cluster, starting_number_cluster)
            numb_of_cluster_remainder = numb_of_cluster
            for c in range(numb_of_cluster):
                if numb_of_cluster_remainder > 10:
                    if int((numb_remainder / numb_of_cluster_remainder) / 1.25) != int(
                            numb_remainder / numb_of_cluster_remainder):
                        numb_of_robot = random.randint(int((numb_remainder / numb_of_cluster_remainder) / 1.25),
                                                       int(numb_remainder / numb_of_cluster_remainder))
                    else:
                        numb_of_robot = numb_remainder / numb_of_cluster
                    starting_number_robot = Aree[numb_aree].Cluster[c].set_robot(numb_of_robot, starting_number_robot)
                    # print('Area:', numb_aree, ' Cluster: ', c, ' Robot : ', numb_of_robot)
                    total_robot = total_robot + numb_of_robot
                    numb_remainder = 90000 - total_robot
                    numb_of_cluster_remainder = numb_of_cluster_remainder - 1
                else:
                    numb_of_robot = int(numb_remainder / numb_of_cluster_remainder)
                    starting_number_robot = Aree[numb_aree].Cluster[c].set_robot(numb_of_robot, starting_number_robot)
                    total_robot = total_robot + numb_of_robot
                    numb_remainder = 90000 - total_robot
                    numb_of_cluster_remainder = numb_of_cluster_remainder - 1
            # print(total_robot)


# Creazione oggetti in modo custum
def custum():
    global starting_number_cluster, starting_number_robot, numb_aree
    numb_aree = input('Inserisci il numero di Aree:  ')
    for a in range(aree):
        number_of_cluster = input('Inserisci il numero di cluster per Area numero ' + str(a) + ':  ')
        Aree.append(Area(a))
        starting_number_cluster = Aree[a].set_cluster(number_of_cluster, starting_number_cluster)
        for c in range(len(Aree[a].Cluster)):
            number_of_robot = input('Inserisci il numero di robot per il Cluster numero ' + str(c) + ': ')
            starting_number_robot = Aree[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
        print('Ultimo robot di questa area (' + str(a) + ') ultimo cluster (' + str(starting_number_cluster) + ') : ',
              Aree[a].Cluster[c].Robot[Aree[a].Cluster[c].Number_of_robot - 1].IDRobot)


################################ CREAZIONE MSG ##########################################


def messaggio():
    global numb_aree, num_cluster
    ### Cambio di Stato ###
    # print('Area e di : ',numb_area)
    area = random.randint(0, numb_aree)
    # print('Area random: ', area)
    # print('Cluster e di : ', numb_cluster)
    cluster = random.randint(0, num_cluster[area])
    # print('Cluster random : ', cluster)
    numb_robot = len(Aree[area].Cluster[cluster].Robot)
    # print('Robot e di : ', numb_robot)
    if (numb_robot - 1) == 0 or (numb_robot - 1) < 0:
        robot = 0
    else:
        robot = random.randint(0, numb_robot - 1)
    # print('robot random : ', robot)
    sensor = random.randint(1, 7)
    # print('il sensore e: ', sensor)
    Aree[area].Cluster[cluster].Robot[robot].change_sensor_status("S" + str(sensor))

    ### Creazione del messaggio ###
    msg = Element('Msg')
    robotag = SubElement(msg, 'Robot')
    areatag = SubElement(robotag, 'ID_Area')
    areatag.text = Aree[area].IDArea
    clustertag = SubElement(robotag, 'ID_Cluster')
    clustertag.text = Aree[area].Cluster[cluster].IDCluster
    robotnametag = SubElement(robotag, 'Name_of_Robot')
    robotnametag.text = Aree[area].Cluster[cluster].Robot[robot].IDRobot
    sensorstag = SubElement(robotag, 'Sensors')
    for i in range(7):
        namesensor = 'S' + str(i + 1)
        namesensostag = SubElement(sensorstag, namesensor)
        namesensostag.text = str(Aree[area].Cluster[cluster].Robot[robot].Sensors[namesensor])
    messaggio_text = tostring(msg)
    # file = ElementTree.ElementTree(msg)
    # file.write("esempio-messaggio.xml")
    return messaggio_text


def messaggio_stringa():
    global numb_aree, num_cluster
    ### Cambio di Stato ###
    area = random.randint(0, numb_aree)
    cluster = random.randint(0, num_cluster[area])
    numb_robot = len(Aree[area].Cluster[cluster].Robot)
    if (numb_robot - 1) == 0 or (numb_robot - 1) < 0:
        robot = 0
    else:
        robot = random.randint(0, numb_robot - 1)
    sensor = random.randint(1, 7)
    Aree[area].Cluster[cluster].Robot[robot].change_sensor_status("S" + str(sensor))

    ### Creazione del messaggio ###
    messaggio_text = '<Msg><Robot><ID_Area>' + Aree[area].IDArea + '</ID_Area><ID_Cluster>' + Aree[area].Cluster[
        cluster].IDCluster + '</ID_Cluster><Name_of_Robot>' + Aree[area].Cluster[cluster].Robot[
                         robot].IDRobot + '</Name_of_Robot><Sensors><S1>' + str(
        Aree[area].Cluster[cluster].Robot[robot].Sensors['S1']) + '</S1><S2>' + str(
        Aree[area].Cluster[cluster].Robot[robot].Sensors['S2']) + '</S2><S3>' + str(
        Aree[area].Cluster[cluster].Robot[robot].Sensors['S3']) + '</S3><S4>' + str(
        Aree[area].Cluster[cluster].Robot[robot].Sensors['S4']) + '</S4><S5>' + str(
        Aree[area].Cluster[cluster].Robot[robot].Sensors['S5']) + '</S5><S6>' + str(
        Aree[area].Cluster[cluster].Robot[robot].Sensors['S6']) + '</S6><S7>' + str(
        Aree[area].Cluster[cluster].Robot[robot].Sensors['S7']) + '</S7></Sensors></Robot></Msg>'

    return messaggio_text


################################# INVIO MESSAGGIO #########################################################


def invio():
    r = requests.post("http://httpbin.org/post", data=messaggio_stringa())
    #print(r.status_code, r.reason, r.text)

################################ INVIO MESSAGGIO THREAD ##################################################
exitFlag = 0

def invio_thread(threadName, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        invio()
        print(threadName, ' ', counter)
        counter = counter - 1

########################################## MAIN PROGRAM ###################################################
def main():
    tipico_randomico()
    volte = 0
    while volte < 200:
        volte = volte + 1
        invio()
        print(volte)

def main_thread():
    tipico_randomico()
    thread1 = myThread(1, "Thread-1", 200)
    thread2 = myThread(2, "Thread-2", 200)
    thread3 = myThread(2, "Thread-3", 200)
    thread4 = myThread(2, "Thread-4", 200)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    print("Exiting Main Thread")

def crea():
    timeout = 600
    time_start = time.time()
    while time.time() < time_start + timeout:
        tipico_randomico()
        del Aree[:]
        print ('--------------------------------fine------------------------------------------')
        time.sleep(10)


# profile.run('crea()')
# profile.run('tipico_randomico()')
#profile.run('main()')

profile.run('main_thread()')
