import cv2


def preprocess(img):

    ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    cv2.imshow('im', ret)
    cv2.waitKey()

    return img

def recognize(imagen):

    num = 0

    return num