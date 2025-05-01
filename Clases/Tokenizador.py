import nltk
import os




class Tokenizador:
    def __init__(self,texto,directorio = os.getcwd()):
        self.texto = texto
        self.directorio = directorio
        self.elementos = []
       

    def __iter__(self):
        return iter(self.elementos)

    
    def ajustar_longitud(self):
        def contar_palabras(frase):
            return len(frase.split(' '))

        sentencias = nltk.sent_tokenize(self.texto)

        num_palabras = 0
        longitud_maxima = 100
        num_doc = 1
        rutas = []
        
        
        

        for sentencia in sentencias:
            if contar_palabras(sentencia) + num_palabras > longitud_maxima:
                #Abrimos un nuevo documento
                ruta = f'{self.directorio}/doc{num_doc}.txt'

                with open(f'{self.directorio}/doc{num_doc}.txt','w',encoding='utf-8') as file:
                    file.write("\n".join(self.elementos))
                    ruta=f'{self.directorio}/doc{num_doc}.txt'
                rutas.append(ruta)
                #Incrementamos el num de documento
                num_doc += 1
                #Reseteamos el contenido del document y las palabras
                self.elementos = []
                num_palabras = 0
            else: #En caso de no superar las 100 palabras. Le añadimos la sentencia al contenido del doc.
                self.elementos.append(sentencia)
                num_palabras += contar_palabras(sentencia) #Sumamos las palabras de la sentencia

        if self.elementos: #Para el último doc. hayan las palabras que hayan. Si hay contenido, se guarda
            ruta = f'{self.directorio}/doc{num_doc}.txt'
            with open(f'{self.directorio}/doc{num_doc}.txt','w',encoding='utf-8') as file:
                file.write("\n".join(self.elementos))
            rutas.append(ruta)

        return rutas

       
