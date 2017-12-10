class Area:
    def __init__(self, id_area):
        self.IDArea = "A" + str(id_area)
        self.Number_of_cluster = None
        self.Cluster = []

    def set_cluster(self, number_of_cluster, starting_number_cluster):
        id_cluster = starting_number_cluster
        self.Number_of_cluster = number_of_cluster
        for c in range(number_of_cluster):
            id_cluster = id_cluster + 1
            self.Cluster.append(Cluster(id_cluster))
        return id_cluster


class Cluster:
    def __init__(self, id_cluster):
        self.IDCluster = "C" + str(id_cluster)
        self.Number_of_robot = None
        self.Robot = []

    def set_robot(self, number_of_robot, stating_number_robot):
        id_robot = stating_number_robot
        self.Number_of_robot = number_of_robot
        for r in range(number_of_robot):
            self.Robot.append(Robot(id_robot))
            id_robot = id_robot + 1
        return id_robot


class Robot:
    def __init__(self, id_robot):
        self.IDRobot = "R" + str(id_robot)
        self.Sensors = {'S1': 1, 'S2': 1, 'S3': 1, 'S4': 1, 'S5': 1, 'S6': 1, 'S7': 1}

    def change_sensor_status(self, id_sensor):
        #print(id_sensor + " : " + str(self.Sensors[id_sensor]))
        if self.Sensors[id_sensor] == 1:
            self.Sensors[id_sensor] = 0
        else:
            self.Sensors[id_sensor] = 1
