import json
import random
import System

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
            Aree.append(System.Area(numb_aree))
            starting_number_cluster = Aree[numb_aree].set_cluster(numb_of_cluster, starting_number_cluster)
            for c in range(numb_of_cluster):
                numb_of_robot = random.randint(500, 1000)
                starting_number_robot = Aree[numb_aree].Cluster[c].set_robot(numb_of_robot, starting_number_robot)
                print('Area:', numb_aree, ' Cluster: ', c, ' Robot : ', numb_of_robot)
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
                    print('Area:', numb_aree, ' Cluster: ', c, ' Robot : ', numb_of_robot)
                    total_robot = total_robot + numb_of_robot
                    numb_remainder = 90000 - total_robot
                    numb_of_cluster_remainder = numb_of_cluster_remainder - 1
                else:
                    numb_of_robot = int(numb_remainder / numb_of_cluster_remainder)
                    starting_number_robot = Aree[numb_aree].Cluster[c].set_robot(numb_of_robot, starting_number_robot)
                    total_robot = total_robot + numb_of_robot
                    numb_remainder = 90000 - total_robot
                    numb_of_cluster_remainder = numb_of_cluster_remainder - 1
            print(total_robot)


############################## CREAZIONE JSON #######################################
def crea():
    global numb_aree, num_cluster
    f = {}
    f["Robot"] = []
    for a in range(numb_aree+1):
        for c in range(num_cluster[a]+1):
            for r in range(len(Aree[a].Cluster[c].Robot)):
                f["Robot"].append({
                    "Name_Of_Robot": Aree[a].Cluster[c].Robot[r].IDRobot,
                    "Sensors": [{
                        "S1": str(Aree[a].Cluster[c].Robot[r].Sensors['S1']),
                        "S2": str(Aree[a].Cluster[c].Robot[r].Sensors['S2']),
                        "S3": str(Aree[a].Cluster[c].Robot[r].Sensors['S3']),
                        "S4": str(Aree[a].Cluster[c].Robot[r].Sensors['S4']),
                        "S5": str(Aree[a].Cluster[c].Robot[r].Sensors['S5']),
                        "S6": str(Aree[a].Cluster[c].Robot[r].Sensors['S6']),
                        "S7": str(Aree[a].Cluster[c].Robot[r].Sensors['S7'])}]})
            namefile = Aree[a].IDArea + Aree[a].Cluster[c].IDCluster+".json"
            with open(namefile, 'w') as outfile:
                json.dump(f, outfile)
            f ={}
            f["Robot"] = []
tipico_randomico()
crea()
