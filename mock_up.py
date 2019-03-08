import numpy as np
import cv2
import random

# ----Preprocesa la imagen----

def preproces(imin):

    imout = cv2.blur(imin, (5, 5))

    return imout


# ----Localiza numeros----

def locnum(A):

    n = random.randint(4, 5)  # Se elige aleatoriamente si hay 4 o 5 cifras
    roi = np.zeros((n, 4))  # Matriz nx4coordenadas (x0,y0, x1, y1) = (coord. sup. izda, coord. inf. dcha.)
    ancho = 85
    alto = 128
    randomcol = random.randint(0, 10)  # Coordenada columna aleatoria de comienzo
    randomrow = random.randint(200, 510)
    roi[0, :] = [randomrow, randomcol, randomrow+alto, randomcol+ancho]  # Coordenada inicial (FILA, COLUMNA)!!!!!

    # Calculo el resto de coordenadas de los rectangulos
    if n == 5:
        for i in range(1, 3):
            roi[i, :] = [roi[i-1, 0], roi[i-1, 1] + ancho + 3, roi[i - 1, 2], roi[i-1, 3] + ancho + 3]

        roi[3, :] = [roi[2, 0], roi[2, 1] + 30, roi[2, 2], roi[2, 3] + 30]

        for i in range(4, n):
            roi[i, :] = [roi[i-1, 0], roi[i-1, 1] + ancho + 3, roi[i - 1, 2], roi[i-1, 3] + ancho + 3]
    elif n == 4:
        for i in range(1, n):
            roi[i, :] = [roi[i - 1, 0], roi[i - 1, 1] + ancho + 10, roi[i - 1, 2], roi[i - 1, 3] + ancho + 10]

    #print(roi)
    roi = roi.astype(int)

    #  Dibujo los rectangulos
    for x2, x1, x4, x3 in roi:
        cv2.rectangle(A, (x1, x2), (x3, x4), (0, 255, 0), 2)  # Para dibujar es al revés (COLUMNA, FILA)

    #cv2.imshow('im', A)
    #cv2.waitKey()

    return roi, A


# ----Lee numeros----

def readnum(s):

    # Generamos 4 o 5 numeros aleatorios de manera que:
    # entre 0 y 10 = 1, entre 11 y 20 = 2... etc

    numeros = np.zeros(s)

    for i in range(s):
        num = random.randint(0, 100)
        if num < 11:
            numeros[i] = 0
        elif 11 <= num < 21:
            numeros[i] = 1
        elif 21 <= num < 31:
            numeros[i] = 2
        elif 31 <= num < 41:
            numeros[i] = 3
        elif 41 <= num < 51:
            numeros[i] = 4
        elif 51 <= num < 61:
            numeros[i] = 5
        elif 61 <= num < 71:
            numeros[i] = 6
        elif 71 <= num < 81:
            numeros[i] = 7
        elif 81 <= num < 91:
            numeros[i] = 8
        else:
            numeros[i] = 9

    return numeros.astype(int)

# ----Almacena numeros----

def save(numeros, path):

    path = '/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales/CrotalesTest/numeros.txt'
    with open(path, 'a') as archivo:
        archivo.write(str(numeros) + '\n')
    archivo.close()
