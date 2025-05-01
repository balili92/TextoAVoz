import gtts
from Tokenizador import Tokenizador
import os
from pydub import AudioSegment #Para seccionar los audios y luego juntarlos en un único archivo
import glob



def borrar_documentos(directorio,patron):
    patron = os.path.join(directorio, patron)
    for archivo in glob.glob(patron):
        os.remove(archivo)


def abrir_archivo(ruta):
    with open(ruta,'r', encoding='utf-8') as file:
        text = file.read()

    return text



class ConvertidorTextoAVoz:
    def __init__(self,texto,directorio = os.getcwd()):
        self.texto = texto
        self.directorio = directorio

   

    def generar_audio_textolargo(self):
        
        txt_tok = Tokenizador(self.texto)
        texto_ajustado = txt_tok.ajustar_longitud()
        audios = []
        for i,archivo in enumerate(texto_ajustado):
            txt = abrir_archivo(archivo)
            print(f"[INFO] Generando audio para el fragmento {i+1}...")

            txt_voz = gtts.gTTS(txt,lang='es')
            audio_path = os.path.join(self.directorio,f"audio{i+1}.mp3")
            txt_voz.save(audio_path)

            audio = AudioSegment.from_mp3(audio_path) #Convertimos el archivo de audio en pydub
            audios.append(audio) #Lo añadimos a la lista, para luego concatenarlos
       
        print(f"[INFO] Total de audios generados: {len(audios)}")
        if audios:
            audio_final = audios[0]
            for audio in audios[1:]:
                audio_final += audio
            print("[INFO] Audios concatenados.")

            audio_final_path = os.path.join(self.directorio, 'audiofinal.mp3')
            audio_final.export(audio_final_path, format='mp3')
    
            borrar_documentos(self.directorio, '*.txt')
            for file in os.listdir(self.directorio):
                if file.startswith("audio") and file.endswith(".mp3") and file != "audiofinal.mp3":
                    os.remove(os.path.join(self.directorio, file))
            
            return audio_final_path


            
        else:
            raise RuntimeError("No se generaron audios. Verifica que el texto haya sido correctamente dividido.")
      
    def generar_audio_textocorto(self):
            
        txt = gtts.gTTS(self.texto, lang = 'es') #Convertimos un texto en audio
        audio_path = os.path.join(self.directorio,('audio.mp3'))
        txt.save(audio_path)
        return audio_path
    


            