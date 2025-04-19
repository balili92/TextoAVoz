import sys
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel
from PyQt5.QtCore import QTimer

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

        self.cargar_button = QPushButton('Cargar archivo', self)
        self.cargar_button.clicked.connect(self.cargar_archivo)
        self.layout.addWidget(self.cargar_button)

        self.reproducir_button = QPushButton('Reproducir', self)
        self.reproducir_button.setEnabled(False)
        self.reproducir_button.clicked.connect(self.reproducir_audio)
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

    def cargar_archivo(self):
        # Abrir un diálogo para seleccionar un archivo
        archivo, _ = QFileDialog.getOpenFileName(self, 'Seleccionar archivo de audio', '', 'Archivos MP3 (*.mp3)')
        
        if archivo:
            self.archivo = archivo
            self.label.setText(f'Archivo cargado: {archivo.split("/")[-1]}')
            self.reproducir_button.setEnabled(True)
            self.pausar_button.setEnabled(True)
            self.detener_button.setEnabled(True)

    def reproducir_audio(self):
        if self.archivo:
            pygame.mixer.music.load(self.archivo)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    reproductor = Reproductor()
    reproductor.show()
    sys.exit(app.exec_())