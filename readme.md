# 🎧 Conversor de Texto a Voz
🗣️ Convierte textos, URLs y PDFs en audios MP3 con una interfaz gráfica amigable




## 📚 Descripción
Este proyecto convierte contenido textual en archivos de audio utilizando tecnología de Text-to-Speech (TTS). Es ideal para crear audios a partir de:

📝 Texto manual

🌐 Artículos web (mediante URL)

📄 Archivos PDF

También incluye un sistema de tokenización para dividir textos largos antes de generar el audio.

## ✨ Características
Función	Descripción
🔊 Conversión TTS	Convierte texto a audio MP3 usando gTTS
✂️ Tokenización	Divide textos >100 palabras en fragmentos para asegurar buena conversión
📂 Soporte de formatos	Entrada desde texto manual, URLs, PDF y reproducción de MP3
🎛️ Interfaz Gráfica (GUI)	Usa PyQt5 para facilitar la interacción del usuario
🎵 Reproducción de Audio	Control de reproducción con pygame

## 🧰 Tecnologías Usadas
Herramienta	Uso
Python	Lenguaje principal
nltk	Tokenización de texto
gTTS	Conversión texto a voz
PyQt5	Interfaz gráfica
pygame	Reproducción de audio
newspaper3k	Extracción de texto desde sitios web
PyMuPDF (fitz)	Lectura y extracción de texto desde PDFs

## 🗂️ Estructura del Proyecto

├── Clases/
│   ├── ConvertidorTextoAVoz.py     # Lógica de conversión TTS
│   ├── Tokenizador.py              # División de texto largo
│   ├── DocumentoPdf.py             # Lectura de archivos PDF
│   ├── ArticuloWeb.py              # Lectura de artículos web
│   └── TextoFuente.py              # Clase base de fuentes de texto
│
├── interfaz/
│   ├── main.py                     # Interfaz gráfica
│   ├── resources/                  # Recursos visuales
│   └── assets/                     # Iconos e imágenes
│
├── ejemplo_audio.mp3               # Ejemplo generado
├── requirements.txt                # Dependencias del proyecto
└── README.md                       # Este archivo
## ▶️ Cómo Usar
1. Instala las dependencias
bash
Copiar
Editar
pip install -r requirements.txt
2. Inicia la aplicación
bash
Copiar
Editar
python interfaz/main.py
3. Selecciona una fuente de texto
✍️ Escribe texto manual

🔗 Ingresa una URL

📁 Sube un PDF

4. Genera y reproduce el audio
✅ Presiona el botón Generar Audio

🔊 Controla la reproducción (play, pausa, stop)

## 🧠 Comportamiento del Tokenizador
Si el texto supera las 100 palabras, se fragmenta automáticamente.

Cada fragmento se convierte en un archivo de audio separado.

Los archivos temporales se eliminan tras la conversión.

## ⚠️ Manejo de Errores
Situación	Acción del sistema
❌ Texto vacío o no válido	Muestra mensaje de error
🌐 URL incorrecta o no accesible	Notificación al usuario
📄 PDF ilegible	Error manejado con mensaje informativo

## 🤝 Contribuciones
¡Las contribuciones son bienvenidas!
Abre un pull request con tus mejoras y asegúrate de probar antes de enviar.


