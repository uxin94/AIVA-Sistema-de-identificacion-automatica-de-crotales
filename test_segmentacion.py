import unittest
from unittest import TestCase
from recognize import Recognizer
from roi import roi
import cv2

# Test que comprueba que las coordenadas del bounding box obtenidas por el algoritmo están
# dentro de un rango de +- 12 pixeles respecto las coordenadas obtenidas manualmente

class TestSegmentacion(TestCase):

    def test_segmentacionok(self):

        A = cv2.imread('/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales/im_Test_seg.png')
        gris = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)
        r = Recognizer()
        roi0 = r._locnum(gris)  # Obtengo la roi de la imagen (coordenadas (x1, x2, y1, y2))

        roi1 = roi(120, 483, 303, 461)  # Coordenadas reales medidas de la imagen de test

        print('Coordenadas manuales: [{}. {}, {}, {}]'.format(roi0[0], roi0[1], roi0[2], roi0[3]))
        print('Coordenadas calculadas por el algoritmo: [{}. {}, {}, {}]'.format(roi1.x0, roi1.x1, roi1.y0, roi1.y1))

        self.assertIn(roi0[0], range(roi1.x0 - 12, roi1.x0 + 12))
        self.assertIn(roi0[1], range(roi1.x1 - 12, roi1.x1 + 12))
        self.assertIn(roi0[2], range(roi1.y0 - 12, roi1.y0 + 12))
        self.assertIn(roi0[3], range(roi1.y1 - 12, roi1.y1 + 12))


if __name__ == '__main__':
    unittest.main()