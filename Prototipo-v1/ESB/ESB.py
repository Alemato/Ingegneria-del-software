import json
import System


starting_number_cluster = 0
starting_number_robot = 0
Area = []
aree = input('Inserisci il numero di Aree:  ')

# Creazioni oggetti
for a in range(aree):
    number_of_cluster = input('Inserisci il numero di cluster per Area numero ' + str(a) + ':  ')
    Area.append(System.Area(a))
    starting_number_cluster = Area[a].set_cluster(number_of_cluster, starting_number_cluster)
    for c in range(len(Area[a].Cluster)):
        number_of_robot = input('Inserisci il numero di robot per il Cluster numero ' + str(c) + ': ')
        starting_number_robot = Area[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
    print('Ultimo robot di questa area (' + str(a) + ') ultimo cluster (' + str(starting_number_cluster) + ') :')
    print(Area[a].Cluster[c].Robot[Area[a].Cluster[c].Number_of_robot -1].IDRobot)
