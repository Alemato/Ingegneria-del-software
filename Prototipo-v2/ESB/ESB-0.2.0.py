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
        invio_thread(self.name, self.counter, self.area)


#################################### CREAZIONE OGGETTI IN MODO MANUALE ##########################################
def custum():
    global starting_number_cluster, starting_number_robot, total_robot
    numb_aree = int(input('Inserisci il numero di Aree:  '))
    for a in range(numb_aree):
        number_of_cluster = int(input('Inserisci il numero di cluster per Area numero ' + str(a) + ':  '))
        Aree.append(System.Area(a))
        starting_number_cluster = Aree[a].set_cluster(number_of_cluster, starting_number_cluster)
        for c in range(len(Aree[a].Cluster)):
            number_of_robot = int(input('Inserisci il numero di robot per il Cluster numero ' + str(c) + ': '))
            starting_number_robot = Aree[a].Cluster[c].set_robot(number_of_robot, starting_number_robot)
            total_robot = total_robot + number_of_robot
    print('risultato della creazione')
    for a in range(numb_aree):
        for c in range(len(Aree[a].Cluster)):
            print('Area:', a, ' Cluster: ', c, ' Robot : ', len(Aree[a].Cluster[c].Robot))
    print('Numero totale di robot al interno del sistema e :  ', total_robot)
    print(len(Aree))


#################################### CREAZIONE OGGETTI IN MODO SEMIRANDOM ##########################################
def tipico_semirandomico():
    global numb_aree, starting_number_robot, starting_number_cluster, total_robot, num_cluster
    numb_of_robot_input = int(input('inserisci il numero di robot del intero sistema:  '))
    print('inizio la creazione')
    print('risultato creazione')
    while total_robot < numb_of_robot_input:
        if total_robot < (numb_of_robot_input / 2):
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
            numb_remainder = numb_of_robot_input - total_robot
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
                    numb_remainder = numb_of_robot_input - total_robot
                    numb_of_cluster_remainder = numb_of_cluster_remainder - 1
                else:
                    numb_of_robot = int(numb_remainder / numb_of_cluster_remainder)
                    starting_number_robot = Aree[numb_aree].Cluster[c].set_robot(numb_of_robot, starting_number_robot)
                    total_robot = total_robot + numb_of_robot
                    numb_remainder = numb_of_robot_input - total_robot
                    numb_of_cluster_remainder = numb_of_cluster_remainder - 1
            print('Numero totale di robot al interno del sistema e :  ', total_robot)


########################### CREAZIONE OGGETTI  IN MODO RANDOMICO CON 90000 ROBOT #################################
def tipico_randomico():
    global numb_aree, starting_number_robot, starting_number_cluster, total_robot, num_cluster
    print('inizio la creazione')
    print('risultato creazione')
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
            print('Numero totale di robot al interno del sistema e :  ', total_robot)


############################## MANUTENZIONE ROBOT ########################################
def manutenzione(robot_name):
    trovato = 0
    for a in range(len(Aree)):
        for c in range(len(Aree[a].Cluster)):
            for r in Aree[a].Cluster[c].Robot:
                if r.IDRobot == robot_name:
                    trovato = 1
                    r.Sensors = {'S1': 1, 'S2': 1, 'S3': 1, 'S4': 1, 'S5': 1, 'S6': 1,
                                 'S7': 1}
                    messaggio = urllib.parse.urlencode(
                        {"ID_Area": Aree[a].IDArea, "ID_Cluster": Aree[a].Cluster[c].IDCluster,
                         "Name_Of_Robot": r.IDRobot,
                         "S1": str(r.Sensors['S1']),
                         "S2": str(r.Sensors['S2']),
                         "S3": str(r.Sensors['S3']),
                         "S4": str(r.Sensors['S4']),
                         "S5": str(r.Sensors['S5']),
                         "S6": str(r.Sensors['S6']),
                         "S7": str(r.Sensors['S7'])})
                    invio(messaggio)
    if trovato == 1:
        return False
    else:
        return True

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
    if len(Aree) - 1 > 0:
        area = random.randint(0, len(Aree) - 1)
    else:
        area = 0
    if len(Aree[area].Cluster) - 1 > 0:
        cluster = random.randint(0, len(Aree[area].Cluster) - 1)
    else:
        cluster = 0
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
    ################ CONNESIONE SERVER 1 #####################
    conn = http.client.HTTPConnection("localhost")
    conn.request("POST", "/httpHandler.php", msg, headers)
    conn.close()

    ################ CONNESIONE SERVER 2 #####################
    # conn1 = http.client.HTTPConnection("localhost")
    # conn1.request("POST", "/httpHandler.php", msg, headers)
    # conn1.close()

    ################ CONNESIONE SERVER 3 #####################
    # conn2 = http.client.HTTPConnection("localhost")
    # conn2.request("POST", "/httpHandler.php", msg, headers)
    # conn2.close()


exitFlag = 0


def invio_thread(threadName, counter, areen):
    while counter:
        if exitFlag:
            threadName.exit()
        invio(messaggio_thread(areen))
        # counter = counter - 1


#################### MAIN PROGRAM #############################
def main():
    uscita = 1
    while uscita:
        opzione_numero = input(
            'inserisci 1 per opzione custom, 2 per opzione tipico semirandomico, 3 per opzione tipico randomico e 4 per aiuto:  ')
        if opzione_numero == '1':
            print('Costruiamo il sitema, rispondi alle seguneti domande')
            custum()
            uscita = 0
        elif opzione_numero == '2':
            print('Costruiamo il sitema, rispondi alla segunete domanda')
            tipico_semirandomico()
            uscita = 0
        elif opzione_numero == '3':
            print('sto costruendo il sistema attendere')
            tipico_randomico()
            uscita = 0
            print('fine costruzione')
        elif opzione_numero == '4':
            print('opzione custom permette di creare il sistema in modo totalmente manuale')
            print(
                'opzione tipico semirandomico permette di creare il sistema in modo semiautomatica ti verra richiesto solo il numero dei robot al interno del sistema')
            print('opzione tipico randomico permette di creare il sistema in modo automatico e totalmente randomico')
        else:
            print('errore non so cosa vuoi, riproviamo')
    print('inizio invio dati')
    while True:
        main_thread()


def main_thread():
    thread1 = myThread(1, "Thread-1", True, Aree)
    thread2 = myThread(2, "Thread-2", True, Aree)
    thread1.start()
    thread2.start()
    while thread1.isAlive() or thread2.isAlive():
        opzione_numero = input(
            'inserisci 1 per effettuare la manutenzione di un robot per terminare il programma premere ctr + c: ')
        if opzione_numero == '1':
            print('hai scelto di effetuare la mautenzione ')
            robot_name = input('inserisci il nome id del robot al quale vuoi effettuare la manutenzione: ')
            while manutenzione(robot_name):
                print('non trovato')
                robot_name = input('inserisci un nome id valido: ')
                manutenzione(robot_name)
            print('trovato')
            print('manutenzione effettuata')
            print('invio i dati in corso...')
        else:
            print('non ho capito')
            print('invio i dati in corso...')
    thread1.join()
    thread2.join()


main()
