import cv2
import numpy as np
import pytesseract
from PIL import Image
from imutils import contours

def recognize(im):
    imC = preprocess(im)
    bbox = locnum(imC)
    numeros = readnum(bbox, imC)

    return numeros

def preprocess(img):
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gris, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernel1 = np.ones((5, 5), np.uint8)
    kernel2 = np.ones((3, 3), np.uint8)

    dil = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel2)

    op = cv2.morphologyEx(dil, cv2.MORPH_ERODE, kernel1)

    cv2.imshow('im', op)
    cv2.waitKey(0)

    return dil


def locnum(img):
    digit = []

    im, contf, hier = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont = contours.sort_contours(contf, method = 'left-to-right')[0]

    for i in cont:

        x, y, w, h = cv2.boundingRect(i)

        if w > 50 and (h > 70 and h<200):
            digit.append(np.asarray([x, x+w, y, y+h]))

            cv2.rectangle(img,(x,y), (x+w, y+h), (128, 200, 0), 2)

    #cv2.drawContours(img, digit, -1, (128, 200, 0), 2)

    cv2.imshow('im', img)
    cv2.waitKey(0)

    return digit

def readnum(digit, img):

    numeros = []
    a=0

    for i in digit:
        x = i[0]
        x2 = i[1]
        y = i[2]
        y2 = i[3]
        imagen = img[y:y2, x:x2]
        a+=1
        config = ('-l eng --oem 1 --psm 7')
        numeros.append(pytesseract.image_to_string(Image.fromarray(imagen), config=config))

    return numeros
