from subprocess import call
from threading import Thread
from sys import argv as arg
from time import sleep

class Instalador(Thread):
    def __init__(self,modulo):
        self.modulo = modulo

        Thread.__init__(self)
    
    def run(self):
        try:
            call(f"pip install {self.modulo}",shell=True)
        except:
            sleep(20)
            call(f"pip install {self.modulo}",shell=True)

threads = []

modulos = arg[1:]

if len(arg) == 2 and arg[1].endswith(".txt"):
    leitor = open(arg[1],"r")

    for mod in leitor:
        threads.append(Instalador(mod))

else:
    for mod in modulos:
        threads.append(Instalador(mod))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()