import cv2
from recognize import Recognizer


#A = cv2.imread('/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales/CrotalesTest/Imagenes/Test/0002.TIF')
A = cv2.imread('/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales/CrotalesTest/TestSamples/0003.TIF')
r = Recognizer()
roi0 = r.recognize(A)
print(roi0)