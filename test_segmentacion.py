import unittest
from unittest import TestCase
from Crotales.mock_up import locnum
from roi import roi
import numpy as np
import cv2


class TestPreprocesado(TestCase):

    def test_segmentacionok(self): #Comprobamos que hay elementos verdes en la imagen (los rectangulos)

        A = cv2.imread('/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales/Crotal1.TIF')
        roi0, _ = locnum(A)

        if roi0.shape[0] == 4:

            roi1 = roi(271, 118, 397, 203)  # Primer rectangulo
            roi2 = roi(271, 218, 397, 302)
            roi3 = roi(271, 316, 397, 402)
            roi4 = roi(271, 416, 397, 502)

            self.assertIn(roi0[0, 0], range(roi1.y0 - 10, roi1.y0 + 10))
            self.assertIn(roi0[0, 1], range(roi1.x0 - 10, roi1.x0 + 10))
            self.assertIn(roi0[0, 2], range(roi1.y1 - 10, roi1.y1 + 10))
            self.assertIn(roi0[0, 3], range(roi1.x1 - 10, roi1.x1 + 10))

            self.assertIn(roi0[1, 0], range(roi2.y0 - 10, roi2.y0 + 10))
            self.assertIn(roi0[1, 1], range(roi2.x0 - 10, roi2.x0 + 10))
            self.assertIn(roi0[1, 2], range(roi2.y1 - 10, roi2.y1 + 10))
            self.assertIn(roi0[1, 3], range(roi2.x1 - 10, roi2.x1 + 10))

            self.assertIn(roi0[2, 0], range(roi3.y0 - 10, roi3.y0 + 10))
            self.assertIn(roi0[2, 1], range(roi3.x0 - 10, roi3.x0 + 10))
            self.assertIn(roi0[2, 2], range(roi3.y1 - 10, roi3.y1 + 10))
            self.assertIn(roi0[2, 3], range(roi3.x1 - 10, roi3.x1 + 10))

            self.assertIn(roi0[3, 0], range(roi4.y0 - 10, roi4.y0 + 10))
            self.assertIn(roi0[3, 1], range(roi4.x0 - 10, roi4.x0 + 10))
            self.assertIn(roi0[3, 2], range(roi4.y1 - 10, roi4.y1 + 10))
            self.assertIn(roi0[3, 3], range(roi4.x1 - 10, roi4.x1 + 10))

        else:

            roi1 = roi(286, 75, 423, 149)  # Primer rectangulo
            roi2 = roi(286, 153, 423, 229)
            roi3 = roi(286, 276, 423, 345)
            roi4 = roi(286, 345, 423, 416)
            roi5 = roi(286, 417, 423, 492)

            self.assertIn(roi0[0, 0], range(roi1.y0 - 10, roi1.y0 + 10))
            self.assertIn(roi0[0, 1], range(roi1.x0 - 10, roi1.x0 + 10))
            self.assertIn(roi0[0, 2], range(roi1.y1 - 10, roi1.y1 + 10))
            self.assertIn(roi0[0, 3], range(roi1.x1 - 10, roi1.x1 + 10))

            self.assertIn(roi0[1, 0], range(roi2.y0 - 10, roi2.y0 + 10))
            self.assertIn(roi0[1, 1], range(roi2.x0 - 10, roi2.x0 + 10))
            self.assertIn(roi0[1, 2], range(roi2.y1 - 10, roi2.y1 + 10))
            self.assertIn(roi0[1, 3], range(roi2.x1 - 10, roi2.x1 + 10))

            self.assertIn(roi0[2, 0], range(roi3.y0 - 10, roi3.y0 + 10))
            self.assertIn(roi0[2, 1], range(roi3.x0 - 10, roi3.x0 + 10))
            self.assertIn(roi0[2, 2], range(roi3.y1 - 10, roi3.y1 + 10))
            self.assertIn(roi0[2, 3], range(roi3.x1 - 10, roi3.x1 + 10))

            self.assertIn(roi0[3, 0], range(roi4.y0 - 10, roi4.y0 + 10))
            self.assertIn(roi0[3, 1], range(roi4.x0 - 10, roi4.x0 + 10))
            self.assertIn(roi0[3, 2], range(roi4.y1 - 10, roi4.y1 + 10))
            self.assertIn(roi0[3, 3], range(roi4.x1 - 10, roi4.x1 + 10))

            self.assertIn(roi0[4, 0], range(roi5.y0 - 10, roi5.y0 + 10))
            self.assertIn(roi0[4, 1], range(roi5.x0 - 10, roi5.x0 + 10))
            self.assertIn(roi0[4, 2], range(roi5.y1 - 10, roi5.y1 + 10))
            self.assertIn(roi0[4, 3], range(roi5.x1 - 10, roi5.x1 + 10))


if __name__ == '__main__':
    unittest.main()