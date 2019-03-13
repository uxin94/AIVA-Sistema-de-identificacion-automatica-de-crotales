import unittest
from unittest import TestCase
from Crotales.numeros import numeros
from Crotales.recognize import Recognizer
import cv2


class TestReadnum(TestCase):

    def test_numeros_iguales(self):

        A = cv2.imread('/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales/Crotal1.TIF')
        num1 = numeros(1, 2, 3, 4)
        r = Recognizer()
        num2 = r._locnum(A)

        # llamar a la funcion que "lee los numeros"
        self.assertEqual(num1.a, num2[0])
        self.assertEqual(num1.b, num2[1])
        self.assertEqual(num1.c, num2[2])
        self.assertEqual(num1.d, num2[3])


    def test_numeros_diferentes(self):
        A = cv2.imread('/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales/Crotal1.TIF')
        num1 = numeros(1, 2, 3, 4)
        r = Recognizer()
        num2 = r._locnum(A)

        # llamar a la funcion que "lee los numeros"
        self.assertNotEqual(num1.a, num2[0])
        self.assertNotEqual(num1.b, num2[1])
        self.assertNotEqual(num1.c, num2[2])
        self.assertNotEqual(num1.d, num2[3])



if __name__ == '__main__':
    unittest.main()