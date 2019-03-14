import unittest
from unittest import TestCase
from numeros import numeros
from recognize import Recognizer
import cv2

# Test que compara la cadena de números obtenida por el algoritmo, con la cadena real del crotal.

class TestReadnum(TestCase):

    def test_numeros_iguales(self):

        A = cv2.imread('/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales/im_Test_seg.png')
        Agris = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)
        roi1 = [120, 483, 303, 461]

        r = Recognizer()
        num2 = r._readnum(roi1, Agris)

        num1 = numeros(0, 0, 5, 4)

        print('Números reales: {}{}{}{}'.format(num1.a, num1.b, num1.c, num1.d))
        print('Números obtenidos por el algoritmo: {}{}{}{}'.format(num2[0], num2[1], num2[2], num2[3]))

        self.assertEqual(str(num1.a), num2[0])
        self.assertEqual(str(num1.b), num2[1])
        self.assertEqual(str(num1.c), num2[2])
        self.assertEqual(str(num1.d), num2[3])


if __name__ == '__main__':
    unittest.main()