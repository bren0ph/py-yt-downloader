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

    def run(self):
        try:
            # baixa o vídeo
            self.stream.download(output_path=self.saida,filename=f'{self.link.title}.mp4')

            # converte para mp3
            tempVideo = os.path.join(self.saida,"%s.mp4" % (self.link.title))
            saidaMp3 = os.path.join(self.saida,f"%s.mp3" % (self.link.title))
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

# abre o arquivo com os links
videos = open('links.txt','r',encoding="utf-8")
threads = []

for video in videos:
    print(video)
    dados = video.strip().split(sep='\t') # o \t é o TAB
    link = dados[0]
    nome = u'%s' % (dados[1])
    autor = u'%s' % (dados[2])
    threads.append(Baixador(link,nome,autor))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()