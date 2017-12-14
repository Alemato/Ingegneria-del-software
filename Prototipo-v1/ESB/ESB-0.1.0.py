import profile
import requests
import random
import threading
import time
import socket
from System import *

Aree = []
total_robot = 0
numb_aree = 0
starting_number_robot = 0
starting_number_cluster = 0
num_cluster = []


########################### CREAZIONE OGGETTI #################################
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
    messaggio_json = {"ID_Area": Aree[area].IDArea, "ID_Cluster": Aree[area].Cluster[cluster].IDCluster,
                      "Name_Of_Robot": Aree[area].Cluster[cluster].Robot[robot].IDRobot,
                      "S1": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S1']),
                      "S2": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S2']),
                      "S3": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S3']),
                      "S4": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S4']),
                      "S5": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S5']),
                      "S6": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S6']),
                      "S7": str(Aree[area].Cluster[cluster].Robot[robot].Sensors['S7'])}
    print(messaggio_json)
    return messaggio_json



####################### INVIO DATI ######################################à
def invio(messaggio):
    r = requests.post("http://192.168.64.2/httpHandler.php", data=messaggio)
    #print(r.status_code, r.reason)
    #print(r.text)


#################### MAIN PROGRAM #############################
def main():
    tipico_randomico()
    invio()

messaggio_j = {"ID_Area": "A1",
               "ID_Cluster": "C67",
               "Name_Of_Robot": "R49270",
               "S1": "1",
               "S2": "0",
               "S3": "1",
               "S4": "1",
               "S5": "1",
               "S6": "1",
               "S7": "1"
               }

def more():
    c = 200
    while c > 0:
        c -= 1
        invio(messaggio_j)
#tipico_randomico()




profile.run('more()')
