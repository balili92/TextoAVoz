Proyecto: Conversor de Texto a Voz con Tokenización y Soporte de Archivos
Descripción
Este proyecto tiene como objetivo principal convertir textos en archivos de audio utilizando la tecnología de conversión de texto a voz (TTS). El sistema admite diversos tipos de fuentes de texto, como entradas manuales, artículos de la web (mediante URLs) y documentos en formato PDF. Además, implementa la tokenización del texto para asegurarse de que los textos largos se fragmenten adecuadamente antes de convertirlos en audio.

Características principales
Conversión de Texto a Voz: Convierte el texto proporcionado en archivos de audio en formato MP3.

Tokenización: Si el texto es demasiado largo, el sistema lo divide en fragmentos para no superar el límite de palabras por archivo de audio.

Soporte de múltiples formatos: Se soportan diferentes tipos de archivos de entrada como:

Texto ingresado manualmente.

Artículos web (utilizando URLs).

Archivos PDF (extraído del contenido del archivo).

Archivos MP3 (para reproducción directa).

Interfaz de Usuario: Interfaz gráfica para seleccionar archivos, controlar la reproducción y generar audios de manera fácil.

Tecnologías usadas
Python: Lenguaje de programación principal.

nltk: Para tokenizar y procesar el texto en fragmentos.

gTTS (Google Text-to-Speech): Para convertir el texto en archivos de audio en formato MP3.

PyQt5: Para la interfaz gráfica de usuario (GUI).

pygame: Para la reproducción del audio generado.

newspaper3k: Para extraer el texto de los artículos web.

PyMuPDF (fitz): Para leer y extraer texto de archivos PDF.

Estructura del Proyecto
bash
Copiar
Editar
├── Clases/
│ ├── ConvertidorTextoAVoz.py # Lógica para convertir texto a audio
│ ├── Tokenizador.py # Lógica para tokenizar textos largos
│ ├── DocumentoPdf.py # Lógica para leer documentos PDF
│ ├── ArticuloWeb.py # Lógica para leer artículos web
│ └── TextoFuente.py # Clase base para fuentes de texto
├── interfaz/
│ ├── main.py # Código para la interfaz gráfica de usuario (GUI)
│ ├── resources/ # Archivos y recursos para la interfaz
│ └── assets/ # Archivos estáticos (como imágenes o iconos)
├── requirements.txt # Dependencias del proyecto
├── README.md # Este archivo
└── ejemplo_audio.mp3 # Ejemplo de archivo generado
Cómo usar el proyecto
Instalar las dependencias:

Primero, asegúrate de tener Python instalado. Luego, instala las dependencias necesarias utilizando pip:

bash
Copiar
Editar
pip install -r requirements.txt
Iniciar la aplicación:

Una vez que las dependencias estén instaladas, puedes ejecutar la interfaz gráfica:

bash
Copiar
Editar
python interfaz/main.py
Seleccionar una fuente de texto:

Si deseas ingresar el texto manualmente, puedes hacerlo en el cuadro de texto proporcionado.

Si tienes un artículo web, simplemente ingresa la URL en el cuadro correspondiente.

Si tienes un archivo PDF, selecciona el archivo en el cuadro de diálogo.

Generar el audio:

Después de seleccionar o ingresar el texto, presiona el botón para generar el audio. El sistema convertirá el texto en un archivo de audio y lo reproducirá automáticamente.

Reproducir el audio:

Una vez generado, el audio se puede reproducir, pausar o detener usando los botones disponibles en la interfaz.

Comportamiento del Tokenizador
Si el texto excede las 100 palabras, el sistema lo divide en fragmentos de texto más pequeños y guarda cada fragmento en un archivo de texto separado.

Luego, convierte cada archivo de texto en un archivo de audio MP3.

Los archivos de texto generados temporalmente se eliminan después de la conversión a audio.

Manejo de errores
Si el texto no es accesible o está vacío, el sistema mostrará un mensaje de error y no generará ningún archivo de audio.

En el caso de los artículos web, si la URL no es válida o no se puede procesar, se notificará al usuario.

Requisitos
Python 3.x

Dependencias:

nltk

gTTS

pygame

PyQt5

newspaper3k

PyMuPDF

Contribuciones
Si deseas contribuir al proyecto, puedes hacerlo enviando un pull request a través de GitHub. Asegúrate de realizar pruebas antes de enviar cambios significativos.

Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.
