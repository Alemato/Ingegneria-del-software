import random
import System

total_robot = 90000

total_robot_per_cluster_tipico = 900
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
    aree = random.randint(1, 2)
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
                    number_of_robot = random.randint(600, 900)
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
                    if c < (len(Area[a].Cluster)/2):
                        number_of_robot = random.randint(400, 900)
                        starting_number_robot = Area[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
                        total_robot = total_robot + number_of_robot
                    elif (c+1) == len(Area[a].Cluster):
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

# custum()

# tipico()

# custom_randomico()

tipico_randomico()