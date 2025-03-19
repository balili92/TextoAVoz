import nltk
import os
import glob


def contar_palabras(frase):
    return len(frase.split(' '))


def ajustar_longitud_texto(texto):
    #Tokenizamos el text, para dividirlo por sentencias
    sentencias = nltk.sent_tokenize(texto)

    num_palabras = 0
    longitud_maxima = 100
    num_doc = 1
    contenido_documento = []

 #Recorremos cada sentencia y contamos el número de palabras

    for sentencia in sentencias:
        directorio = os.getcwd()
        if contar_palabras(sentencia) + num_palabras > longitud_maxima:
            #Abrimos un nuevo documento
            with open(f'{directorio}/doc{num_doc}.txt','w',encoding='utf-8') as file:
                file.write("\n".join(contenido_documento))
            #Incrementamos el num de documento
            num_doc += 1
            #Reseteamos el contenido del document y las palabras
            contenido_documento = []
            num_palabras = 0
        else: #En caso de no superar las 100 palabras. Le añadimos la sentencia al contenido del doc.
            contenido_documento.append(sentencia)
            num_palabras += contar_palabras(sentencia) #Sumamos las palabras de la sentencia

    if contenido_documento: #Para el último doc. hayan las palabras que hayan. Si hay contenido, se guarda
        with open(f'{directorio}/doc{num_doc}.txt','w',encoding='utf-8') as file:
            file.write("\n".join(contenido_documento))

            

def borrar_documentos(directorio,patron):
    patron = os.path.join(directorio, patron)
    for archivo in glob.glob(patron):
        os.remove(archivo)

