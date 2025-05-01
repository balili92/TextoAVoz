from TextoFuente import TextoFuente
from newspaper import Article
from ConvertidorTextoAVoz import ConvertidorTextoAVoz
from Tokenizador import Tokenizador


class ArticuloWeb(TextoFuente):

    def __init__(self, texto):
        super().__init__(texto)

    def obtener_texto(self):
        article = Article(self.texto)
        try:
            article.download()
            article.parse()
            texto = article.text
            return texto

        except Exception as e:
                print('Error al descargar el artículo',e)

        
    

