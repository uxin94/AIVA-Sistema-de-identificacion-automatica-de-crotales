import cv2
import numpy as np
import pytesseract
from PIL import Image
from imutils import contours

class Recognizer:

    def recognize(self, im):

        imC = self._preprocess(im)
        bbox = self._locnum(imC)
        numeros = self._readnum(bbox, imC)

        return numeros

    def _preprocess(self, img):  # Preprocesa la imagen

        gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        [f, c] = np.shape(gris)

        #_, thresh = cv2.threshold(gris, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        z1 = gris.reshape((f*c, 1))
        z = np.float32(z1)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        flags = cv2.KMEANS_RANDOM_CENTERS
        compactness, labels, centers = cv2.kmeans(z, 3, None, criteria, 10, flags)
        #print(centers)
        thresh1 = np.logical_and(gris >= centers[1]-30, gris <= centers[1]+30)
        thresh = np.array(thresh1 * 1 * 255, dtype=np.uint8)
        #cv2.imshow('umbral', thresh)
        #cv2.waitKey(0)

        kernel1 = np.ones((5, 5), np.uint8)
        kernel2 = np.ones((3, 3), np.uint8)

        #dil = thresh
        dil = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel2)
        op = cv2.morphologyEx(dil, cv2.MORPH_ERODE, kernel1)

        cv2.imshow('im', op)
        cv2.waitKey(0)

        return op

    def _locnum(self, img):  # Encuentra los numeros

        digit = []

        im, contf, hier = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cont = contours.sort_contours(contf, method = 'left-to-right')[0]

        for i in cont:

            x, y, w, h = cv2.boundingRect(i)

            if w > 50 and (h > 70 and h<200):
                digit.append(np.asarray([x, x+w, y, y+h]))

        digit = np.asarray(digit)
        resta = digit[0, 2] - digit[-1, 2]
        if resta < 0: # Inclinada hacia abajo derecha
            y1 = digit[0, 2]
            y2 = digit[-1, 3]
            x1 = digit[0, 0]
            x2 = digit[-1, 1]

        else:  # Inclinada hacia arriba (izquierda)
            y1 = digit[-1, 2] #FILA
            y2 = digit[0, 3]
            x1 = digit[0, 0]#COLUMNA
            x2 = digit[-1, 1]

        imagen = img[y1:y2, x1:x2]
        cv2.imshow('imagen_recortada', imagen)
        cv2.waitKey(0)

        return digit

    def _readnum(self, digit, img):  # Lee los numeros

        numeros = []

        for i in digit:
            x = i[0]
            x2 = i[1]
            y = i[2]
            y2 = i[3]
            imagen = img[y:y2, x:x2] #(COLUMNA, FILA)
            config = '--psm 10 -c tessedit_char_whitelist=.0123456789'
            numeros.append(pytesseract.image_to_string(Image.fromarray(imagen), config=config))

        return numeros