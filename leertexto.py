import gtts
import os
from tokenizador import borrar_documentos

def leer_texto(texto):
    #Funcion que después de pasarle un texto, lo reproduce
    directorio = os.getcwd()
    txt = gtts.gTTS(texto, lang = 'es') #Convertimos un texto en audio
    audio_path = os.path.join(directorio,('audio.mp3'))
    txt.save(audio_path)
    os.system(f"mpg123 {'audio.mp3'}")
    borrar_documentos(directorio, '*.mp3')
    
