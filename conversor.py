from subprocess import call as cmd
from os import listdir
from threading import Thread

# apaga qualquer arquivo .py na pasta de telas, incluindo o construtor
cmd("del /s /q telas\*.py",shell=True)

# seção de conversão de .ui para .py
# função de conversão adaptada para multithreading
class Conversor(Thread):
    def __init__(self,arquivo,saida):
        self.arquivo = arquivo
        self.saida = saida
        Thread.__init__(self)
    
    def run(self):
        cmd(f"pyside6-uic {self.arquivo} -g python -o {self.saida}",shell=True)
        print(f"Arquivo {self.saida.replace('telas/','')} criado")

inp = [x for x in listdir('telas/') if x.endswith('.ui')]
inp = [f"telas/{x}" for x in inp]
outp = [x.replace('.ui','.py') for x in inp]

# variável das threads
threads = []

# adiciona as classes de thread para a variável threads
for x in range(len(inp)):
    threads.append(Conversor(inp[x],outp[x]))

# começa a converter as threads
for thread in threads:
    thread.start()

# faz o código principal esperar que todas as threads terminem
for thread in threads:
    thread.join()

# seção de importação através do arquivo construtor
# preparação dos arquivos
init = open("telas/__init__.py","a")
arquivos = [x.replace('telas/','.') for x in outp]
arquivos = [x.replace('.py','') for x in arquivos]

# escrita das importações no arquivo construtor
for i in range(len(outp)):
    leitor = open(f"telas/{arquivos[i]}.py".replace("/.",'/'),"r")
    classe = ''
    for linha in leitor:
        if linha.startswith('class'):
            classe = linha.split(sep=' ')[1]
            break
    classe = classe[:classe.index('(')]
    init.write(f"from {arquivos[i]} import {classe}\n")
    leitor.close()

init.close()
print("Arquivo construtor pronto")