import cv2
import numpy as np
import pytesseract
from PIL import Image
from imutils import contours
import matplotlib.pyplot as plt

class Recognizer:

    def recognize(self, imagen):

        imC = self._preprocess(imagen)
        roi = self._locnum(imC)
        numeros = self._readnum(roi, imC)

        return numeros

    def _preprocess(self, img):  # Preprocesa la imagen

        gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        hist = plt.hist(gris.flatten(), bins='auto')
        # Obtenemos el primer minimo del histograma, el limite inferior del umbral
        minimo = hist[0][0:15].argmin() + 1
        pos = hist[1][int(minimo)]

        # Umbralizamos la imagen desde la posicion anterior a +60
        thresh1 = np.logical_and(gris >= pos, gris <= pos + 60)
        thresh = np.array(thresh1 * 255, dtype=np.uint8)

        # Erosion + cierre
        kernel1 = np.ones((5, 5), np.uint8)
        kernel2 = np.ones((3, 3), np.uint8)
        dil = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel2)
        op = cv2.morphologyEx(dil, cv2.MORPH_ERODE, kernel1)

        return op

    def _locnum(self, img):  # Encuentra los numeros

        digit = []

        im, contf, hier = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cont = contours.sort_contours(contf, method='left-to-right')[0]

        for i in cont:

            x, y, w, h = cv2.boundingRect(i)

            if w > 50 and (h > 70 and h<200):
                digit.append(np.asarray([x, x+w, y, y+h]))

        digit = np.asarray(digit)
        resta = digit[0, 2] - digit[-1, 2]
        if resta < 0:  # Inclinada hacia abajo derecha
            y1 = digit[0, 2]
            y2 = digit[-1, 3]
            x1 = digit[0, 0]
            x2 = digit[-1, 1]

        else:  # Inclinada hacia arriba (izquierda)
            y1 = digit[-1, 2]  # FILA
            y2 = digit[0, 3]
            x1 = digit[0, 0]  # COLUMNA
            x2 = digit[-1, 1]

        roi = [x1, x2, y1, y2]

        return roi

    def _readnum(self, roi, im):  # Lee los numeros

        imagen = im[roi[2]:roi[3], roi[0]:roi[1]]

        config = '--psm 8 -c tessedit_char_whitelist=0123456789'
        numeros = (pytesseract.image_to_string(Image.fromarray(imagen), config=config))

        return numeros