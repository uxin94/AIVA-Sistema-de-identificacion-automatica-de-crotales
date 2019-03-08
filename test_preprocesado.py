import unittest
from unittest import TestCase
from Crotales.mock_up import preproces
import numpy as np
import cv2

class TestPreprocesado(TestCase):

    def test_im_preprocesada(self):

        path = '/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales'
        imprec = cv2.imread(path+'/0002_proc.TIF')  # Leo la imagen procesada ok
        imin = cv2.imread(path+'/0002_proc.TIF')  # Leo la imagen original
        imout = preproces(imin)  # Proceso la imagen original
        dif = np.sum(abs(imout-imprec))  # La imagen procesada debe ser lo mas parecida a la procesada ok
        self.assertIn(dif, range(20))  # Comprobamos que las imagenes sean parecidas


if __name__ == '__main__':
    unittest.main()