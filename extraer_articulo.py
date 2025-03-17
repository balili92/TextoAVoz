'''Script que selecciona un artículo a partir de una url y lo convierte en un texto'''
#importamos los módulos necesarios
from newspaper import Article #para extraer el artículo


def extraer_articulo(url):
    article = Article(url)
    try:
        article.download()
        article.parse()
        texto = article.text
        return texto
    
    except Exception as e:
        print('Error al descargar el artículo',e)





url = 'https://elpais.com/salud-y-bienestar/2025-02-25/david-glowacki-fisico-la-idea-de-vivir-500-anos-me-asusta-mas-que-la-muerte.html'
texto = extraer_articulo(url)

 


