from ventana_ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog
import sys
import os
from tokenizador import borrar_documentos
from intento_clases import TextoPlano,TextoURL, TextoPDF


class MiVentana(QMainWindow, Ui_ReproductorDeTextos, QTextEdit):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz gráfica
    #Lógica de botones
        self.pushButton.clicked.connect(self.reproducir_texto)
       

    def reproducir_texto(self):
    #Funcion que después de pasarle un texto, lo reproduce
            texto = self.textEdit.toPlainText()
            directorio = os.getcwd()
            if texto.startswith('https://'):
                texto = TextoURL(texto)
                texto.generar_audios()

            elif texto.endswith('.pdf'):
                ruta = self.textEdit.toPlainText()
                texto = TextoPDF(ruta)
                txt = texto.extraer_texto(ruta)
                texto.leer_texto()
            else:
                texto = TextoPlano(texto)
                texto.leer_texto()

   
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Ejecuta la aplicación
    
    
