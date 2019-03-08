import unittest
from unittest import TestCase
import random
from Crotales.numeros import numeros
from Crotales.mock_up import readnum


class TestReadnum(TestCase):

    def test_numeros_iguales(self):

        num1 = numeros(1, 2, 3, 4, 5)
        n = random.randint(4, 5)
        num2 = readnum(n)

        if n == 4:
            #llamar a la funcion que "lee los numeros"
            self.assertEqual(num1.a, num2[0])
            self.assertEqual(num1.b, num2[1])
            self.assertEqual(num1.c, num2[2])
            self.assertEqual(num1.d, num2[3])
        else:
            self.assertEqual(num1.a, num2[0])
            self.assertEqual(num1.b, num2[1])
            self.assertEqual(num1.c, num2[2])
            self.assertEqual(num1.d, num2[3])
            self.assertEqual(num1.e, num2[4])


    def test_numeros_diferentes(self):

        num1 = numeros(1, 2, 3, 4, 5)
        n = random.randint(4, 5)
        num2 = readnum(n)

        if n == 4:
            #llamar a la funcion que "lee los numeros"
            self.assertNotEqual(num1.a, num2[0])
            self.assertNotEqual(num1.b, num2[1])
            self.assertNotEqual(num1.c, num2[2])
            self.assertNotEqual(num1.d, num2[3])
        else:
            self.assertNotEqual(num1.a, num2[0])
            self.assertNotEqual(num1.b, num2[1])
            self.assertNotEqual(num1.c, num2[2])
            self.assertNotEqual(num1.d, num2[3])
            self.assertNotEqual(num1.e, num2[4])




if __name__ == '__main__':
    unittest.main()