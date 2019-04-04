# Sistema de identificación automática de crotales

Este proyecto, destinado al sector ganadero, consiste en realizar una fotografía a un crotal de una vaca y, tras procesarla y analizarla, obtener el número de identificación. 

# Puesta en marcha

Para utilizar este sistema se requiere la instalación de:
- Python 3.7
- OpenCV 3.4.5.20 (pip install opencv-contrib-python)
- Numpy 1.15.2 (pip install numpy)
- pytesseract 0.2.6 (pip install pytesseract)
- imutils 0.5.2 (pip install imutils)
- Pillow 5.3.0 (pip install Pillow)

Para descargar el código se debe ejecutar la siguiente línea en consola: 
git clone https://github.com/uxin94/AIVA-Sistema-de-identificacion-automatica-de-crotales.git

A continuación, un ejemplo de cómo ejecutar el programa:

$ python3
>from recognize import Recognizer

>import cv2

>imagen = cv2.imread('/path/imagen.TIF')

>r = Recognizer()

>r.recognize(imagen)

Por otra parte, para probar el funcionamiento del algoritmo se han desarrollado tres test:
- Preprocesado de la imagen: $ python3 test_preprocesado.py 

- Localizador de números: $ python3 test_segmentacion.py 

- Identificador de números: $ python3 test_numeros.py


# Despliegue de la aplicación cliente/servidor

Como la aplicación móvil aún no se ha desarrollado, es necesario ejecutar el código del cliente en sí. 
Para ello, se ha de seguir los siguientes pasos:

- Es necesaria la instalación de Python 3.7 y de OpenCV 3.4.5.20 (pip install opencv-
contrib-python).
- Descagar el archivo Cliente.py.
- Desde terminal ejecutar el siguiente comando: python3 Cliente.py --image_path='path a la imagen/imagen.TIF'. Siendo image_path la ruta de la imagen que se quiere analizar.
