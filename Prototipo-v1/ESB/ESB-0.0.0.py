from xml.etree.ElementTree import *
import profile
#import requests
import random
import time
from System import *

Aree = []
total_robot = 0
numb_aree = 0
starting_number_robot = 0
starting_number_cluster = 0

# Creazione oggetti in modo strettamente tipico
# def tipico():
#     starting_number_cluster = 0
#     starting_number_robot = 0
#     total_cluster_tipoco = 100
#     total_robot_per_cluster_tipico = 900
#     Area.append(System.Area(0))
#     Area[0].set_cluster(total_cluster_tipoco, starting_number_cluster)
#     for c in range(len(Area[0].Cluster)):
#         starting_number_robot = Area[0].Cluster[c].set_robot(total_robot_per_cluster_tipico, starting_number_robot)
#     #print('Ultimo robot di questa area (' + str(0) + ') ultimo cluster (' + str(starting_number_cluster) + ') : ',
#           #Area[0].Cluster[c].Robot[Area[0].Cluster[c].Number_of_robot - 1].IDRobot)


# Creazione oggetti in modo custum randomico
def tipico_randomico():
    numb_aree = 0
    starting_number_robot = 0
    starting_number_cluster = 0
    total_robot = 0
    while total_robot < 90000:
        if total_robot < 50000:
            numb_of_cluster = random.randint(20, 50)
            Aree.append(Area(numb_aree))
            starting_number_cluster = Aree[numb_aree].set_cluster(numb_of_cluster, starting_number_cluster)
            for c in range(numb_of_cluster):
                numb_of_robot = random.randint(500, 1000)
                starting_number_robot = Aree[numb_aree].Cluster[c].set_robot(numb_of_robot, starting_number_robot)
                #print('Area:', numb_aree, ' Cluster: ', c, ' Robot : ', numb_of_robot)
                total_robot =total_robot + numb_of_robot
            numb_aree = numb_aree + 1
        else:
            #print('-------------------------------')
            #print('numero di robot : ', total_robot)
            #print('-------------------------------')
            break

    return total_robot




# Creazione oggetti in modo custum randomico
# def custom_randomico():
#     starting_number_cluster = 0
#     starting_number_robot = 0
#     aree = random.randint(1, 3)  #######################################
#     for a in range(aree):
#         number_of_cluster = random.randint(1, 100)  #######################################
#         Area.append(System.Area(a))
#         starting_number_cluster = Area[a].set_cluster(number_of_cluster, starting_number_cluster)
#         for c in range(len(Area[a].Cluster)):
#             number_of_robot = random.randint(1, 900)  #########################################
#             starting_number_robot = Area[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
#         print('Ultimo robot di questa area (' + str(a) + ') ultimo cluster (' + str(starting_number_cluster) + ') : ',
#               Area[a].Cluster[c].Robot[Area[a].Cluster[c].Number_of_robot - 1].IDRobot)


# Creazione oggetti in modo custum
# def custum():
#     starting_number_cluster = 0
#     starting_number_robot = 0
#     aree = input('Inserisci il numero di Aree:  ')
#     for a in range(aree):
#         number_of_cluster = input('Inserisci il numero di cluster per Area numero ' + str(a) + ':  ')
#         Area.append(System.Area(a))
#         starting_number_cluster = Area[a].set_cluster(number_of_cluster, starting_number_cluster)
#         for c in range(len(Area[a].Cluster)):
#             number_of_robot = input('Inserisci il numero di robot per il Cluster numero ' + str(c) + ': ')
#             starting_number_robot = Area[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
#         print('Ultimo robot di questa area (' + str(a) + ') ultimo cluster (' + str(starting_number_cluster) + ') : ',
#               Area[a].Cluster[c].Robot[Area[a].Cluster[c].Number_of_robot - 1].IDRobot)

################################ CREAZIONE MSG ##########################################


def messaggio():
    ### Cambio di Stato ###
    numb_area = len(Area)
    #print('Area e di : ',numb_area)
    if (numb_area - 1) == 0 or (numb_area - 1) < 0:
        area = 0
    else:
        area = random.randint(0, numb_area - 1)
    #print('Area random: ', area)
    numb_cluster = len(Area[area].Cluster)
    #print('Cluster e di : ', numb_cluster)
    if (numb_cluster - 1) == 0 or (numb_cluster - 1) < 0:
        cluster = 0
    else:
        cluster = random.randint(0, numb_cluster - 1)
    #print('Cluster random : ', numb_cluster)
    numb_robot = len(Area[area].Cluster[cluster].Robot)
    #print('Robot e di : ', numb_robot)
    if (numb_robot - 1) == 0 or (numb_robot - 1) < 0:
        robot = 0
    else:
        robot = random.randint(0, numb_robot - 1)
    #print('robot random : ', robot)
    sensor = random.randint(1, 7)
    #print('il sensore e: ', sensor)
    Area[area].Cluster[cluster].Robot[robot].change_sensor_status("S" + str(sensor))

    ### Creazione del messaggio ###
    msg = Element('Msg')
    robotag = SubElement(msg, 'Robot')
    areatag = SubElement(robotag, 'ID_Area')
    areatag.text = Area[area].IDArea
    clustertag = SubElement(robotag, 'ID_Cluster')
    clustertag.text = Area[area].Cluster[cluster].IDCluster
    robotnametag = SubElement(robotag, 'Name_of_Robot')
    robotnametag.text = Area[area].Cluster[cluster].Robot[robot].IDRobot
    sensorstag = SubElement(robotag, 'Sensors')
    for i in range(7):
        namesensor = 'S' + str(i + 1)
        namesensostag = SubElement(sensorstag, namesensor)
        namesensostag.text = str(Area[area].Cluster[cluster].Robot[robot].Sensors[namesensor])
    messaggio_text = tostring(msg)
    #file = ElementTree.ElementTree(msg)
    #file.write("esempio-messaggio.xml")
    return messaggio_text


################################# INVIO MESSAGGIO #########################################################


def invio():
    r = requests.post("http://localhost:8088/", data=messaggio())
    print(r.status_code, r.reason)


########################################## MAIN PROGRAM ###################################################
def main():
    tipico()
    volte = 0
    while volte < 90000:
        volte = volte + 1
        #print(messaggio())



def crea():
    timeout = 3600
    time_start = time.time()
    numb1 = 0
    while time.time() < time_start + timeout:
        numb = tipico_randomico()
        del Aree[:]
        if numb > numb1:
            numb1 = numb
            print(numb1)

profile.run('crea()')