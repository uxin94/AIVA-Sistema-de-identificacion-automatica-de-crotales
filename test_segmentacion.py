import unittest
from unittest import TestCase
from Crotales.mock_up import locnum
import numpy as np
import cv2

class TestPreprocesado(TestCase):

    def test_im_preprocesada(self): #Comprobamos que hay elementos verdes en la imagen (los rectangulos)

        path = '/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales/CrotalesTest/TestSamples/0001.TIF'
        imin = cv2.imread(path)
        _, imout = locnum(imin)
        verde = np.array([0, 255, 0])
        mascara = cv2.inRange(imout, verde, verde)
        self.assertTrue(sum(sum(mascara)) != 0)


if __name__ == '__main__':
    unittest.main()