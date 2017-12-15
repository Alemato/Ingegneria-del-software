import profile
import requests
import random
import threading
import time
import socket
from System import *



class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, se):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.s = se

    def run(self):
        #print("Starting " + self.name)
        invio_thread(self.name,self.counter, self.s)
        #print("Exiting " + self.name)

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


def sessione():
    s = requests.Session()
    return s

def invio(s):
    s.post("http://localhost/httpHandler.php", data=messaggio_j, headers={'content-type': 'application/json'})
exitFlag = 0

def invio_thread(threadName, counter, s):
    while counter:
        if exitFlag:
            threadName.exit()
        invio(s)
        counter = counter - 1

def more():

    c = 1500
    while c > 0:
        c -= 1
        invio(s)

def more_thread():
    s1 = sessione()
    thread1 = myThread(1, "Thread-1", 93, s1)
    thread2 = myThread(2, "Thread-2", 93, s1)
    thread3 = myThread(3, "Thread-3", 93, s1)
    thread4 = myThread(4, "Thread-4", 93, s1)
    thread5 = myThread(5, "Thread-5", 94, s1)
    thread6 = myThread(6, "Thread-6", 94, s1)
    thread7 = myThread(7, "Thread-7", 94, s1)
    thread8 = myThread(8, "Thread-8", 94, s1)
    thread9 = myThread(9, "Thread-9", 94, s1)
    thread10 = myThread(10, "Thread-10", 94, s1)
    thread11 = myThread(11, "Thread-11", 94, s1)
    thread12 = myThread(12, "Thread-12", 94, s1)
    thread13 = myThread(13, "Thread-13", 94, s1)
    thread14 = myThread(14, "Thread-14", 94, s1)
    thread15 = myThread(15, "Thread-15", 94, s1)
    thread16 = myThread(16, "Thread-16", 94, s1)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread11.start()
    thread12.start()
    thread13.start()
    thread14.start()
    thread15.start()
    thread16.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()
    thread11.join()
    thread12.join()
    thread13.join()
    thread14.join()
    thread15.join()
    thread16.join()
profile.run('more_thread()')