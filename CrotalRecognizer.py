import cv2
import recognize

path = '/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales'
im = cv2.imread(path+'/0002.TIF')
num = recognize(im)