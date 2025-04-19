import os
import subprocess
import signal
import fitz
import gtts
from tokenizador import borrar_documentos, ajustar_longitud_texto #Tokenizar el texto

from newspaper import Article #para extraer el artículo
import glob

from pydub import AudioSegment #Para seccionar los audios y luego juntarlos en un único archivo

def borrar_documentos(directorio,patron):
        patron = os.path.join(directorio, patron)
        for archivo in glob.glob(patron):
            os.remove(archivo)

class TextoPlano():
    def __init__(self,texto):
        self.texto = texto
    
    def leer_texto(self):
    #Funcion que después de pasarle un texto, lo reproduce
        directorio = os.getcwd()
        txt = gtts.gTTS(self.texto, lang = 'es') #Convertimos un texto en audio
        audio_path = os.path.join(directorio,('audio.mp3'))
        txt.save(audio_path)
        os.system(f'mpg123 {'audio.mp3'}')
        borrar_documentos(directorio, '*.mp3')

   

class TextoURL():
    def __init__(self,texto):
        self.texto = texto
    
        #Extraemos el texto de la url
        article = Article(self.texto)
        try:
            article.download()
            article.parse()
            self.texto = article.text

        except Exception as e:
                print('Error al descargar el artículo',e)
    
    def archivo_to_txt(self, ruta_archivo):
        with open(ruta_archivo,'r') as file:
            text = file.read()
    
        return text

    def generar_audios(self):
        lista_archivos = ajustar_longitud_texto(self.texto) #Creamos los archivos.txt
        directorio = os.getcwd() #directorio actual

        audios = [] #Inicializamos una lista vacía para ir añadiendo los audios
        for i, archivo in enumerate(lista_archivos):
            txt = self.archivo_to_txt(archivo)
            tts = gtts.gTTS(txt,lang='es')
            audio_path = os.path.join(directorio,f'audio{i+1}.mp3')
            tts.save(audio_path)
        
            audio = AudioSegment.from_mp3(audio_path) #Convertimos el archivo de audio en pydub
            audios.append(audio) #Lo añadimos a la lista, para luego concatenarlos

        audio_final = sum(audios)
        audio_final_path = os.path.join(directorio,f'audiofinal.mp3')
        audio_final.export(audio_final_path,format='mp3') #Guardamos el archivo final de audios concatenados
        os.system(f'mpg123 {'audiofinal.mp3'}')
        # borrar_documentos(directorio,'*.mp3')
        borrar_documentos(directorio,'*.txt')

class TextoPDF():
    def __init__(self,ruta):
        self.ruta = ruta
    
    def extraer_texto(self,ruta):
        with open(ruta, "rb") as f: #Abrimos el archivo en modo binario
            f = fitz.open(stream=f.read(), filetype="pdf")
            self.texto = ""
            for pagina in f: #vamos añadiendo el texto
                self.texto += pagina.get_text()
            return self.texto
            

    def leer_texto(self):
    #Funcion que después de pasarle un texto, lo reproduce
        directorio = os.getcwd()
        txt = gtts.gTTS(self.texto, lang = 'es') #Convertimos un texto en audio
        audio_path = os.path.join(directorio,('audio.mp3'))
        mp3 = txt.save(audio_path)
        return mp3
       


        
   



