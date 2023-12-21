# importa os módulos necessários
import os
from threading import Thread
from pytube import YouTube as yt
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
from eyed3 import load

# classe que vai baixar o vídeo, converter para MP3 320kbps e adicionar metadados
class Baixador(Thread):
    def __init__(self,link,nome,autor):
        self.link = yt(link)
        self.stream = self.link.streams.filter(only_audio=True,file_extension="mp4").first()
        self.saida = "saida/"
        self.nome = u'%s' % (nome)
        self.autor = u'%s' % (autor)
        Thread.__init__(self)

    # executa o processo de download
    def run(self):
        try:
            # baixa o vídeo
            self.stream.download(output_path=self.saida,filename=f'{self.link.title}.mp4')

            # converte para mp3
            tempVideo = os.path.join(self.saida,"%s.mp4" % (self.link.title))
            saidaMp3 = os.path.join(self.saida,f"%s.mp3" % (self.link.title))

        # caso não consiga salvar com o título do vídeo, salva com o nome informado
        except:
            self.stream.download(output_path=self.saida,filename=f'{self.nome}.mp4')

            tempVideo = os.path.join(self.saida,"%s.mp4" % (self.nome))
            saidaMp3 = os.path.join(self.saida,f"%s.mp3" % (self.nome))
        finally:
            ffmpeg_extract_audio(tempVideo,saidaMp3,bitrate=320)

        # adiciona metadados
        audio = load(saidaMp3)
        audio.tag.title = self.nome
        audio.tag.artist = self.autor

        # salva
        audio.tag.save()
        os.remove(tempVideo)

# modificações para branch da versão de linha de comando (CLI)
videos = []
threads = []

# prepara as threads para os downloads
def baixa():
    for video in videos:
        link = video['link']
        nome = video['nome']
        autor = video['autor']
        threads.append(Baixador(link,nome,autor))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

# coloca um vídeo na lista de download
def adiciona():
    link = input("Link: ")
    nome = input("Nome: ")
    autor = input("Autor: ")

    video = dict(link=link,nome=nome,autor=autor)

    videos.append(video)

# mostra quais vídeos estão prontos para download
def lista():
    print("Indice - Link - Nome - Autor")
    i = 0
    for video in videos:
        print(" - ".join([str(i),video['link'],video['nome'],video['autor']]))
        i += 1

# remove um vídeo da lista
def apaga():
    ind = input("Índice: ")
    del videos[ind]

# menu principal (o coração da branch)
def menu():
    op = 0
    while op < 5:
        print("MENU:")
        print("1 - Adicionar músicas para download")
        print("2 - Listar músicas para download")
        print("3 - Remover música para download")
        print("4 - Iniciar download")
        print("5+ - Sair")
        op = int(input("> "))

        if op == 1:
            adiciona()
        elif op == 2:
            lista()
        elif op == 3:
            apaga()
        elif op == 4:
            baixa()
        else:
            break

menu()