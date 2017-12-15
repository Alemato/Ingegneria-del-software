import profile
import requests
import http.client
import json


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

def invio(s):
    r = requests.post("http://localhost/httpHandler.php", data=messaggio_j)
    print(r.status_code, r.text)
def sessione():
    s = requests.Session()
    return s
import http.client
import json

def invio1():
    connection = http.client.HTTPSConnection('localhost')
    headers = {'Content-type': 'application/json'}
    json_foo = json.dumps(messaggio_j)
    connection.request('POST', '/httpHandler.php', json_foo, headers)
    response = connection.getresponse()
    print(response.read().decode())

def more():
    s = sessione()
    c = 1
    while c > 0:
        c -= 1
        invio(s)
def more1():
    c = 200
    while c > 0:
        c-=1
        invio1()
more1()