import unittest
from unittest import TestCase
from Crotales.mock_up import preproces
import numpy as np
import cv2

class TestPreprocesado(TestCase):

    def test_im_preprocesada(self):

        path = '/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales/CrotalesTest/TestSamples/0001.TIF'
        imin = cv2.imread(path)
        imout = preproces(imin)
        dif = np.sum(abs(imout-imin))
        self.assertTrue(dif != 0)


if __name__ == '__main__':
    unittest.main()