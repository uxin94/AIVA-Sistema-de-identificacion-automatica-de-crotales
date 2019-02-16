import cv2
import numpy as np
from sklearn.utils import shuffle


src_path = '/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales/CrotalesTest/TestSamples'
path = '/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales/CrotalesTest'
gt = '/Users/andrea/Desktop/MASTER/SEGUNDO CUATRI/APLICACIONES/Proyecto crotales/CrotalesTest/GroundTruth.txt'


g = np.genfromtxt(gt, dtype=str, skip_header=1, unpack=False)
a = np.arange(397)
a += 1
b, gtrain = shuffle(a, g)
b -= 1

# Guardamos imagenes de train

for i in range(0, 318):

    if (b[i] == 237) or (b[i] == 238):
        continue

    img = cv2.imread(src_path + '/{}.TIF'.format(str(b[i]+1).zfill(4)))
    cv2.imwrite(path + '/Train/{}.TIF'.format(str(b[i]+1).zfill(4)), img)


traingt = open(path+'/TrainGT.txt', 'w')
traingt.write(str(gtrain[0:318]))
traingt.close


# Guardamos imagenes de test

for i in range(318, 358):

    if (b[i] == 237) or (b[i] == 238):
        continue
    img = cv2.imread(src_path + '/{}.TIF'.format(str(b[i]+1).zfill(4)))
    cv2.imwrite(path + '/Test/{}.TIF'.format(str(b[i]+1).zfill(4)), img)


testgt = open(path+'/TestGT.txt', 'w')
testgt.write(str(gtrain[318:358]))
testgt.close

# Guardamos imagenes de val

for i in range(358, 397):

    if (b[i] == 237) or (b[i] == 238):
        continue

    img = cv2.imread(src_path + '/{}.TIF'.format(str(b[i]+1).zfill(4)))
    cv2.imwrite(path + '/Val/{}.TIF'.format(str(b[i]+1).zfill(4)), img)

valgt = open(path+'/ValGT.txt', 'w')
valgt.write(str(gtrain[358:397]))
valgt.close