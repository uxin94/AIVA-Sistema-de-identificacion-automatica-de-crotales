import unittest
from unittest import TestCase
from recognize import Recognizer
import numpy as np
import cv2

# Test que comprueba que la imagen preprocesada manualmente y la preprocesada por el algoritmo
# difieren en menos de un 15% de pixeles.

class TestPreprocesado(TestCase):

    def test_im_preprocesada(self):

        # Leemos las imagenes
        path = '/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales'
        imprec1 = cv2.imread(path+'/im_test_precok.TIF')  # Imagen procesada manualmente
        imprec = cv2.cvtColor(imprec1, cv2.COLOR_BGR2GRAY)
        imin = cv2.imread(path+'/im_Test_seg.png')  # Imagen original

        # Proceso la imagen original
        r = Recognizer()
        imout = r._preprocess(imin)
        #cv2.imshow('im', imout)
        #cv2.waitKey(0)

        # Obtengo la diferencia de pixeles entre las dos imagenes
        [f, c] = np.shape(imprec)
        pxs = f * c
        dif = np.count_nonzero(imprec-imout)  # Miramos los pixeles que son diferentes entre las dos imagenes
        porc = int((dif * 100) / pxs)  # Obtenemos el porcentaje de pixeles diferentes
        print(porc)
        self.assertIn(porc, range(15))  # Comprobamos que las imagenes sean parecidas


if __name__ == '__main__':
    unittest.main()