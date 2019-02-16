import numpy as np
import cv2
import sys
import random

A = cv2.imread('C:\\Users\\mary\\Desktop\\MOVA\\CuatrimestreII\\Aplicaciones industriales\\Practica\\TestSamples\\0001.TIF')

n = random.randint(4,5)  # Se elige aleatoriamente si hay 4 o 5 cifras
roi = np.zeros((n, 2))  # Matriz nx4coordenadas
ancho = 85
alto = 105
randomcol = random.randint(0, 10)  # Coordenada columna aleatoria de comienzo
randomrow = random.randint(200, 510)
roi[0,:] = [randomrow, randomcol]  # Coordenada inicial

for i in range(1, n):
    roi[i, :] = [roi[0,0], roi[i-1,1]+ancho]

print(roi)
roi = roi.astype(int)

for x2, x1 in roi:
    cv2.rectangle(A, (x1, x2), (x1 + 75, x2 + 130), (0, 255, 0), 2)#dibujar al revés, col-fil

cv2.imshow('im', A)

cv2.waitKey()
