from TextoFuente import TextoFuente
import fitz


class DocumentoPdf(TextoFuente):

    def __init__(self, texto):
        super().__init__(texto)

    def obtener_texto(self):
        with open(self.texto, "rb") as f: #Abrimos el archivo en modo binario
            f = fitz.open(stream=f.read(), filetype="pdf")
            texto = ""
            for pagina in f: #vamos añadiendo el texto
                texto += pagina.get_text()

        return texto
    

