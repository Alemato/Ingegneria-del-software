from xml.etree.ElementTree import *
from xml.etree import ElementTree
import requests
import random
import System

Area = []


# Creazione oggetti in modo strettamente tipico
def tipico():
    starting_number_cluster = 0
    starting_number_robot = 0
    total_cluster_tipoco = 100
    total_robot_per_cluster_tipico = 900
    Area.append(System.Area(0))
    Area[0].set_cluster(total_cluster_tipoco, starting_number_cluster)
    for c in range(len(Area[0].Cluster)):
        starting_number_robot = Area[0].Cluster[c].set_robot(total_robot_per_cluster_tipico, starting_number_robot)
    print('Ultimo robot di questa area (' + str(0) + ') ultimo cluster (' + str(starting_number_cluster) + ') : ',
          Area[0].Cluster[c].Robot[Area[0].Cluster[c].Number_of_robot - 1].IDRobot)


# Creazione oggetti in modo custum randomico
def tipico_randomico():
    total_robot = 0
    starting_number_cluster = 0
    starting_number_robot = 0
    aree = random.randint(1, 3)
    if aree == 1:
        a = 0
        number_of_cluster = 100
        Area.append(System.Area(a))
        starting_number_cluster = Area[a].set_cluster(number_of_cluster, starting_number_cluster)
        for c in range(len(Area[a].Cluster)):
            number_of_robot = 900
            starting_number_robot = Area[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)

        print(
            'Ultimo robot di questa area (' + str(a) + ') ultimo cluster (' + str(starting_number_cluster) + ') : ',
            Area[a].Cluster[c].Robot[Area[a].Cluster[c].Number_of_robot - 1].IDRobot)
    elif aree == 2:
        for a in range(aree):
            if a == 0:
                number_of_cluster = random.randint(40, 100)
                Area.append(System.Area(a))
                starting_number_cluster = Area[a].set_cluster(number_of_cluster, starting_number_cluster)
                for c in range(len(Area[a].Cluster)):
                    number_of_robot = random.randint(500, 1000)
                    starting_number_robot = Area[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
                    total_robot = total_robot + number_of_robot
                print(
                    'Ultimo robot di questa area (' + str(a) + ') ultimo cluster (' + str(
                        starting_number_cluster) + ') : ',
                    Area[a].Cluster[c].Robot[Area[a].Cluster[c].Number_of_robot - 1].IDRobot)
            else:
                number_of_cluster = random.randint(30, 50)
                Area.append(System.Area(a))
                starting_number_cluster = Area[a].set_cluster(number_of_cluster, starting_number_cluster)
                for c in range(len(Area[a].Cluster)):
                    if c < (len(Area[a].Cluster) / 2):
                        number_of_robot = random.randint(500, 1000)
                        starting_number_robot = Area[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
                        total_robot = total_robot + number_of_robot
                    elif (c + 1) == len(Area[a].Cluster):
                        number_of_robot = 90000 - total_robot
                        starting_number_robot = Area[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
                print(
                    'Ultimo robot di questa area (' + str(a) + ') ultimo cluster (' + str(
                        starting_number_cluster) + ') : ',
                    Area[a].Cluster[c].Robot[Area[a].Cluster[c].Number_of_robot - 1].IDRobot)
                print(len(Area[a].Cluster[c].Robot))
    else:
        for a in range(aree):
            if a == 0 or a == 1:
                number_of_cluster = random.randint(30, 50)
                Area.append(System.Area(a))
                starting_number_cluster = Area[a].set_cluster(number_of_cluster, starting_number_cluster)
                for c in range(len(Area[a].Cluster)):
                    number_of_robot = random.randint(500, 1000)
                    starting_number_robot = Area[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
                    total_robot = total_robot + number_of_robot
                print(
                    'Ultimo robot di questa area (' + str(a) + ') ultimo cluster (' + str(
                        starting_number_cluster) + ') : ',
                    Area[a].Cluster[c].Robot[Area[a].Cluster[c].Number_of_robot - 1].IDRobot)
            else:
                number_of_cluster = random.randint(30, 50)
                Area.append(System.Area(a))
                starting_number_cluster = Area[a].set_cluster(number_of_cluster, starting_number_cluster)
                for c in range(len(Area[a].Cluster)):
                    if c < (len(Area[a].Cluster) / 2):
                        number_of_robot = random.randint(500, 1000)
                        starting_number_robot = Area[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
                        total_robot = total_robot + number_of_robot
                    elif (c + 1) == len(Area[a].Cluster):
                        number_of_robot = 90000 - total_robot
                        starting_number_robot = Area[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
                print(
                    'Ultimo robot di questa area (' + str(a) + ') ultimo cluster (' + str(
                        starting_number_cluster) + ') : ',
                    Area[a].Cluster[c].Robot[Area[a].Cluster[c].Number_of_robot - 1].IDRobot)
                print(len(Area[a].Cluster[c].Robot))


# Creazione oggetti in modo custum randomico
def custom_randomico():
    starting_number_cluster = 0
    starting_number_robot = 0
    aree = random.randint(1, 3)  #######################################
    for a in range(aree):
        number_of_cluster = random.randint(1, 100)  #######################################
        Area.append(System.Area(a))
        starting_number_cluster = Area[a].set_cluster(number_of_cluster, starting_number_cluster)
        for c in range(len(Area[a].Cluster)):
            number_of_robot = random.randint(1, 900)  #########################################
            starting_number_robot = Area[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
        print('Ultimo robot di questa area (' + str(a) + ') ultimo cluster (' + str(starting_number_cluster) + ') : ',
              Area[a].Cluster[c].Robot[Area[a].Cluster[c].Number_of_robot - 1].IDRobot)


# Creazione oggetti in modo custum
def custum():
    starting_number_cluster = 0
    starting_number_robot = 0
    aree = input('Inserisci il numero di Aree:  ')
    for a in range(aree):
        number_of_cluster = input('Inserisci il numero di cluster per Area numero ' + str(a) + ':  ')
        Area.append(System.Area(a))
        starting_number_cluster = Area[a].set_cluster(number_of_cluster, starting_number_cluster)
        for c in range(len(Area[a].Cluster)):
            number_of_robot = input('Inserisci il numero di robot per il Cluster numero ' + str(c) + ': ')
            starting_number_robot = Area[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
        print('Ultimo robot di questa area (' + str(a) + ') ultimo cluster (' + str(starting_number_cluster) + ') : ',
              Area[a].Cluster[c].Robot[Area[a].Cluster[c].Number_of_robot - 1].IDRobot)

################################ CREAZIONE MSG ##########################################


def messaggio():
    ### Cambio di Stato ###
    if len(Area) - 1 == 0:
        area = 0
    else:
        area = random.randint(0, len(Area) - 1)
    if len(Area[area].Cluster) - 1 == 0:
        cluster = 0
    else:
        cluster = random.randint(0, len(Area[area].Cluster) - 1)
    if len(Area[area].Cluster[cluster].Robot) - 1 == 0:
        robot = 0
    else:
        robot = random.randint(0, len(Area[area].Cluster[cluster].Robot) - 1)
    sensor = random.randint(1, 7)
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

tipico_randomico()
while True:
    invio()