import profile
import random
import http.client
import urllib.parse
import System
import threading

Aree = []
total_robot = 0
numb_aree = 0
starting_number_robot = 0
starting_number_cluster = 0
num_cluster = []
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, Aree):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.area = Aree

    def run(self):
        #print("Starting " + self.name)
        invio_thread(self.name, self.counter, self.area)
        #print("Exiting " + self.name)

########################### CREAZIONE OGGETTI #################################
def tipico_randomico():
    global numb_aree, starting_number_robot, starting_number_cluster, total_robot, num_cluster
    while total_robot < 90000:
        if total_robot < 50000:
            numb_of_cluster = random.randint(20, 50)
            Aree.append(System.Area(numb_aree))
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
            Aree.append(System.Area(numb_aree))
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


########################### CREAZIONE MESSAGGIO ##########################################
def messaggio():
    global numb_aree, num_cluster
    area = random.randint(0, numb_aree)
    cluster = random.randint(0, num_cluster[area])
    numb_robot = len(Aree[area].Cluster[cluster].Robot)
    if (numb_robot - 1) == 0 or (numb_robot - 1) < 0:
        robot = 0
    else:
        robot = random.randint(0, numb_robot - 1)
    sensor = random.randint(1, 7)
    Aree[area].Cluster[cluster].Robot[robot].change_sensor_status("S" + str(sensor))
    messaggio_json = urllib.parse.urlencode(
        {"ID_Area": Aree[area].IDArea, "ID_Cluster": Aree[area].Cluster[cluster].IDCluster,
         "Name_Of_Robot": Aree[area].Cluster[cluster].Robot[robot].IDRobot,
         "S1": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S1']),
         "S2": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S2']),
         "S3": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S3']),
         "S4": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S4']),
         "S5": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S5']),
         "S6": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S6']),
         "S7": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S7'])})
    return messaggio_json

def messaggio_thread(Areen):
    global numb_aree, num_cluster
    area = random.randint(0, numb_aree)
    cluster = random.randint(0, num_cluster[area])
    numb_robot = len(Areen[area].Cluster[cluster].Robot)
    if (numb_robot - 1) == 0 or (numb_robot - 1) < 0:
        robot = 0
    else:
        robot = random.randint(0, numb_robot - 1)
    sensor = random.randint(1, 7)
    Areen[area].Cluster[cluster].Robot[robot].change_sensor_status("S" + str(sensor))
    messaggio_json = urllib.parse.urlencode(
        {"ID_Area": Areen[area].IDArea, "ID_Cluster": Areen[area].Cluster[cluster].IDCluster,
         "Name_Of_Robot": Areen[area].Cluster[cluster].Robot[robot].IDRobot,
         "S1": str(Areen[area].Cluster[cluster].Robot[robot].Sensors['S1']),
         "S2": str(Areen[area].Cluster[cluster].Robot[robot].Sensors['S2']),
         "S3": str(Areen[area].Cluster[cluster].Robot[robot].Sensors['S3']),
         "S4": str(Areen[area].Cluster[cluster].Robot[robot].Sensors['S4']),
         "S5": str(Areen[area].Cluster[cluster].Robot[robot].Sensors['S5']),
         "S6": str(Areen[area].Cluster[cluster].Robot[robot].Sensors['S6']),
         "S7": str(Areen[area].Cluster[cluster].Robot[robot].Sensors['S7'])})
    return messaggio_json

####################### INVIO DATI ######################################

def invio(msg):
    conn = http.client.HTTPConnection("localhost")
    conn.request("POST", "/httpHandler.php", msg, headers)
    conn.close()

exitFlag = 0

def invio_thread(threadName, counter, areen):
    while counter:
        if exitFlag:
            threadName.exit()
        invio(messaggio_thread(areen))
        counter = counter - 1
#################### MAIN PROGRAM #############################
def main():
    tipico_randomico()
    c = 90000
    while c > 0:
        invio(messaggio())
        c -= 1

def main_thread():
    print('start program...')
    tipico_randomico()
    Aree1 = Aree
    Aree2 = Aree
    thread1 = myThread(1, "Thread-1", 45000, Aree1)
    thread2 = myThread(2, "Thread-2", 45000, Aree2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Exiting Main Thread")

main_thread()
