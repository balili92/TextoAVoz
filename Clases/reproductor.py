import sys
import os
import pygame
from PyQt5.QtWidgets import QTextEdit,QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui
from ArticuloWeb import ArticuloWeb
from ConvertidorTextoAVoz import ConvertidorTextoAVoz
from DocumentoPdf import DocumentoPdf



class Reproductor(QWidget):
    def __init__(self):
        super().__init__()

        # Inicializa Pygame para reproducción de audio
        pygame.mixer.init()

        # Configura la ventana
        self.setWindowTitle('Reproductor de Audio')
        self.setGeometry(300, 300, 300, 150)

        # Variables de control
        self.archivo = None
        self.reproduciendo = False

        # Crear los elementos de la interfaz
        self.layout = QVBoxLayout()
        self.label = QLabel('No se ha cargado ningún archivo', self)
        self.layout.addWidget(self.label)
        self.texto_ruta = QTextEdit(self)
        self.texto_ruta.setPlaceholderText('Escribe tu texto aquí')
        self.layout.addWidget(self.texto_ruta)

        self.cargar_button = QPushButton('Cargar archivo', self)
        self.cargar_button.clicked.connect(self.cargar_archivo)
        self.layout.addWidget(self.cargar_button)

        self.convertir_button = QPushButton('Convertir en audio',self)
        self.layout.addWidget(self.convertir_button)
        self.convertir_button.setEnabled(False)
        self.texto_ruta.textChanged.connect(self.validar_entrada)
        self.convertir_button.clicked.connect(self.convertir)



        self.reproducir_button = QPushButton('Reproducir', self)
        self.reproducir_button.setEnabled(False)
        self.reproducir_button.clicked.connect(self.reproducir_audio)  # Conectar al método de reproducción
        self.layout.addWidget(self.reproducir_button)

        self.pausar_button = QPushButton('Pausar', self)
        self.pausar_button.setEnabled(False)
        self.pausar_button.clicked.connect(self.pausar_audio)
        self.layout.addWidget(self.pausar_button)

        self.detener_button = QPushButton('Detener', self)
        self.detener_button.setEnabled(False)
        self.detener_button.clicked.connect(self.detener_audio)
        self.layout.addWidget(self.detener_button)

        self.setLayout(self.layout)

         #Añadir iconos
        self.reproducir_button.setIcon(QtGui.QIcon("icons/play.svg"))
        self.pausar_button.setIcon(QtGui.QIcon("icons/pause.svg"))
        self.cargar_button.setIcon(QtGui.QIcon("icons/folder-plus.svg"))
        

    def cargar_archivo(self):
        # Abrir un diálogo para seleccionar un archivo
        archivo, _ = QFileDialog.getOpenFileName(self, 'Seleccionar archivo de audio', '', 'Archivos (*.pdf *.mp3)')
        
        if archivo:
            extension = os.path.splitext(archivo)[1].lower()
            if extension == '.mp3':
                self.texto_ruta.setText(archivo)
                self.archivo = archivo
                self.label.setText(f'Archivo cargado: {archivo.split("/")[-1]}')
                self.reproducir_button.setEnabled(True)
                self.pausar_button.setEnabled(True)
                self.detener_button.setEnabled(True)
            elif extension == '.pdf':
                self.texto_ruta.setText(archivo)
                self.label.setText(f'Archivo cargado: {archivo.split("/")[-1]}')
                self.reproducir_button.setEnabled(True)
                self.pausar_button.setEnabled(True)
                self.detener_button.setEnabled(True)



    def validar_entrada(self):
        texto = self.texto_ruta.toPlainText().strip()  # o .text() si es QLineEdit
        if texto.startswith("https://"):
            self.convertir_button.setEnabled(True)
        else:
            self.convertir_button.setEnabled(False)


    def convertir(self):

        texto = self.texto_ruta.toPlainText()
        if texto.startswith("https://"):
            num_palabras = len(texto.split())
            if num_palabras > 100:
                    self.label.setText(f'Generando audio...')
                    txt = ArticuloWeb(texto)
                    texto_audio = txt.obtener_texto()
                    audio = ConvertidorTextoAVoz(texto_audio)  # Convertir el texto a audio
                    mp3 = audio.generar_audio_textolargo()  # Generar el archivo de audio (mp3)
                    pygame.mixer.music.load(mp3)
                    pygame.mixer.music.play()
                    self.reproduciendo = True
                    self.reproducir_button.setEnabled(False)
                    self.pausar_button.setEnabled(True)
                    self.detener_button.setEnabled(True)
            else:
                self.label.setText(f'Generando audio...')
                audio = ConvertidorTextoAVoz(txt)
                mp3 = audio.generar_audio_textocorto()
                pygame.mixer.music.load(mp3)
                pygame.mixer.music.play()
                self.reproduciendo = True
                self.reproducir_button.setEnabled(False)
                self.pausar_button.setEnabled(True)
                self.detener_button.setEnabled(True)
            


    def reproducir_audio(self):
        
        texto = self.texto_ruta.toPlainText()

        if texto.endswith('.mp3'):
            pygame.mixer.music.load(self.archivo)
            pygame.mixer.music.play()
            self.reproduciendo = True
            self.reproducir_button.setEnabled(False)
            self.pausar_button.setEnabled(True)
            self.detener_button.setEnabled(True)

        elif texto.endswith('.pdf'):
                txt = DocumentoPdf(texto)
                texto = txt.obtener_texto()
                audio = ConvertidorTextoAVoz(texto)
                num_palabras = len(texto.split())

                if num_palabras < 100:
                    mp3 = audio.generar_audio_textocorto()
                else:
                    mp3 = audio.generar_audio_textolargo()
                    
                pygame.mixer.music.load(mp3)
                pygame.mixer.music.play()
                self.reproduciendo = True
                self.reproducir_button.setEnabled(False)
                self.pausar_button.setEnabled(True)
                self.detener_button.setEnabled(True)
        else:
            audio = ConvertidorTextoAVoz(texto)
            mp3 = audio.generar_audio_textocorto()
            pygame.mixer.music.load(mp3)
            pygame.mixer.music.play()
            self.reproduciendo = True
            self.reproducir_button.setEnabled(False)
            self.pausar_button.setEnabled(True)
            self.detener_button.setEnabled(True)

        
            

    def pausar_audio(self):
        if self.reproduciendo:
            pygame.mixer.music.pause()
            self.reproduciendo = False
            self.pausar_button.setText('Reanudar')
        else:
            self.label.setText(f'Pausado...')
            pygame.mixer.music.unpause()
            self.reproduciendo = True
            self.pausar_button.setText('Pausar')

    def detener_audio(self):

        pygame.mixer.music.stop()
        self.reproduciendo = False
        self.pausar_button.setEnabled(False)
        self.reproducir_button.setEnabled(True)
        self.detener_button.setEnabled(False)
        self.pausar_button.setText('Pausar')
        self.texto_ruta.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    reproductor = Reproductor()
    reproductor.show()
    sys.exit(app.exec_())


'''https://elpais.com/us/migracion/2025-05-01/trump-vuelve-a-separar-familias-la-deportacion-de-dos-madres-a-cuba-y-venezuela-sin-sus-bebes.html'''