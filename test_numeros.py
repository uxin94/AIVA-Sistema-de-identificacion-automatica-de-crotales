import unittest
from unittest import TestCase
from Crotales.numeros import numeros


class TestReadnum(TestCase):

    def test_numeros_iguales(self):

        num1 = numeros(1, 2, 3, 4)
        num2 = numeros(1, 2, 3, 4)
        self.assertEqual(num1.a, num2.a)
        self.assertEqual(num1.b, num2.b)
        self.assertEqual(num1.c, num2.c)
        self.assertEqual(num1.d, num2.d)

    def test_numeros_diferentes(self):
        num1 = numeros(1, 2, 3, 4)
        num2 = numeros(5, 6, 7, 9)
        self.assertNotEqual(num1.a, num2.a)
        self.assertNotEqual(num1.b, num2.b)
        self.assertNotEqual(num1.c, num2.c)
        self.assertNotEqual(num1.d, num2.d)


if __name__ == '__main__':
    unittest.main()