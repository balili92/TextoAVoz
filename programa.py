from ventana_ui import *
from articulo import extraer_articulo

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.descargar_archivo)
        self.pushButton.clicked.connect(self.guardar_archivo)
    
    
    def descargar_archivo(self):
        self.url = self.lineEdit.text()
        self.txt = extraer_articulo(self.url)
        self.lineEdit.clear()
    
    def guardar_archivo(self):
        guardar_audio(self.txt)
        
  
  
    
    

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
