import cv2
import base64
import json
import http.client
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-pathim", "--image_path", required=True, help="Path where image is")
args = vars(ap.parse_args())
image_path = args['image_path']

img = cv2.imread(image_path)

png_encoded_img = cv2.imencode('.jpg', img)
base64_encoded_img = base64.b64encode(png_encoded_img[1])
message = {'img': base64_encoded_img.decode('UTF-8')}
json_message = json.dumps(message)

# Creamos conexión, cabecera y enviamos el mensaje con un POST
headers = {'Content-type': 'application/json'}
connection = http.client.HTTPConnection('192.168.1.16', port=8000)
connection.request('POST', '', json_message, headers)

# Esperamos la respuesta y la pintamos por pantalla
resp = connection.getresponse()
print(resp.read().decode())