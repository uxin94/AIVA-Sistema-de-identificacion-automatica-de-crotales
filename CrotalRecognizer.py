import cv2
from recognize import recognize


path = 'C:\\Users\\mary\\Desktop\\MOVA\\CuatrimestreII\\Aplicaciones industriales\\Practica\\TestSamples'
im = cv2.imread(path+'\\0382.TIF')

bbox = recognize(im)

print(bbox)


