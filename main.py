import os
from subprocess import call as cmd
from threading import Thread
from PySide6.QtWidgets import *
from pytube import YouTube as yt
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
from eyed3 import load
from telas import *

class Baixador(Thread):
    def __init__(self,link,nome,autor):
        self.link = yt(link)
        self.autor = u'%s' % (autor)
        self.nome = u'%s' % (nome)
        self.saida = "saida/"
        Thread.__init__(self)

    def run(self):
        try:
            # baixa o vídeo
            self.stream = self.link.streams.filter(only_audio=True, file_extension="mp4").first()
            self.stream.download(output_path=self.saida, filename=f'{self.link.title}.mp4')

            # converte para mp3
            tempVideo = os.path.join(self.saida, "%s.mp4" % (self.link.title))
            saidaMp3 = os.path.join(self.saida, f"%s.mp3" % (self.link.title))
        except:
            self.stream.download(output_path=self.saida, filename=f'{self.nome}.mp4')

            tempVideo = os.path.join(self.saida, "%s.mp4" % (self.nome))
            saidaMp3 = os.path.join(self.saida, f"%s.mp3" % (self.nome))
        finally:
            ffmpeg_extract_audio(tempVideo, saidaMp3, bitrate=320)

        # adiciona metadados
        audio = load(saidaMp3)
        audio.tag.title = self.nome
        audio.tag.artist = self.autor

        # salva
        audio.tag.save()
        os.remove(tempVideo)

# modificações da branch de GUI
# janela principal (coração da branch)
class TelaPrincipal(QMainWindow,Ui_Conversor):

    # carrega a tela
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Add.clicked.connect(self.adicionaNaTabela)
        self.Converte.clicked.connect(self.converteMusicas)

    # adiciona os dados do vídeo na tabela
    def adicionaNaTabela(self):

        # acessa os dados dos textfields e prepara para inserção na tabela
        link = QTableWidgetItem(self.Url.text())
        autor = QTableWidgetItem(self.Nome.text())
        nome = QTableWidgetItem(self.Autor.text())

        # acessa a linha e adiciona os dados
        self.Lista.setRowCount(self.Lista.rowCount() + 1)
        linha = self.Lista.rowCount() - 1
        self.Lista.setItem(linha,0,link)
        self.Lista.setItem(linha,2,autor)
        self.Lista.setItem(linha,1,nome)

        # limpa os campos
        self.Url.clear()
        self.Nome.clear()
        self.Autor.clear()

    # limpa a tabela (depois do download)
    def limpaLista(self):
        self.Lista.setRowCount(0)

    # inicia o processo de download
    def converteMusicas(self):
        threads = []

        # cria as threads de download
        for linha in range(self.Lista.rowCount()):
            link = self.Lista.item(linha,0).text()
            nome = self.Lista.item(linha,2).text()
            autor = self.Lista.item(linha,1).text()

            threads.append(Baixador(link,nome,autor))
        
        # manda as threads iniciarem o processo
        for thread in threads:
            thread.start()

        # faz com que a thread principal aguarde o fim das outras threads
        for thread in threads:
            thread.join()

        self.limpaLista()

# carrega a janela principal
if __name__ == '__main__':
    app = QApplication([])
    tela_principal = TelaPrincipal()
    tela_principal.show()
    app.exec()