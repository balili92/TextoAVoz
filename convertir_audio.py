import gtts
from pydub import AudioSegment
import os
from articulo import extraer_articulo
from tokenizador import ajustar_longitud_texto, borrar_documentos


def archivo_to_txt(ruta_archivo):
    with open(ruta_archivo,'r') as file:
        text = file.read()
    
    return text



#Generamos archivos de audio de todos los archivos.txt que tenemos en el directorio
def generar_audios(lista_archivos,directorio):
    audios = [] #Inicializamos una lista vacía para ir añadiendo los audios
    for i, archivo in enumerate(lista_archivos):
        txt = archivo_to_txt(archivo)
        tts = gtts.gTTS(txt,lang='es')
        audio_path = os.path.join(directorio,f'audio{i+1}.mp3')
        tts.save(audio_path)
    
        audio = AudioSegment.from_mp3(audio_path) #Convertimos el archivo de audio en pydub
        audios.append(audio) #Lo añadimos a la lista, para luego concatenarlos

    audio_final = sum(audios)
    audio_final_path = os.path.join(directorio,f'audiofinal.mp3')
    audio_final.export(audio_final_path,format='mp3') #Guardamos el archivo final de audios concatenados


directorio = '/home/balili92/MasterConquerBlocks/PYTHON/PROYECTOS/TXTaVOZ'
archivos_txt = [os.path.abspath(f) for f in os.listdir(directorio) if f.endswith('.txt')]
archivos_ord = sorted(archivos_txt) #Ordenamos los archivos de menor a mayor

url = 'https://elpais.com/salud-y-bienestar/2025-02-25/david-glowacki-fisico-la-idea-de-vivir-500-anos-me-asusta-mas-que-la-muerte.html'
texto = extraer_articulo(url)

borrar_documentos(directorio,'*.txt')
borrar_documentos(directorio,'*.mp3')