import http.client, urllib.parse
import profile

msg = urllib.parse.urlencode({"ID_Area": "A1",
                              "ID_Cluster": "C67",
                              "Name_Of_Robot": "R49270",
                              "S1": "1",
                              "S2": "0",
                              "S3": "1",
                              "S4": "1",
                              "S5": "1",
                              "S6": "1",
                              "S7": "1"
                              })
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

def invio(conn):
    conn.request("POST", "/httpHandler.php", msg, headers)


def more():
    c = 1500
    while c > 0:
        c -= 1
        conn = http.client.HTTPConnection("localhost")
        invio(conn)
    #conn.close()

profile.run('more()')
