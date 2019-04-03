from http.server import BaseHTTPRequestHandler
import socketserver
import base64
import json
import cv2
import cgi
import numpy as np
from recognize import Recognizer

class Servidor(BaseHTTPRequestHandler): # Clase que actua como servidor HTTP

    def _set_headers(self):

    # Método privado que escribe la cabecera de las respuestas
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()


    def do_POST(self):

        # POST Nos envían datos, hacemos la VA y respondemos
        message = self._extract_msg()

        # Primero extraemos la imagen del JSON que debe venir en Base64
        base64_img = message['img']
        jpg_img = base64.b64decode(base64_img)
        img = cv2.imdecode(np.fromstring(jpg_img, dtype=np.uint8), -1)

        # Luego llamamos a nuestra fachada para que aplique la VA
        r = Recognizer()
        result = r.recognize(img)

        # Finalmente escribimos el resultado en un mapa para enviarlo
        message2 = result
        bytes_message = bytes(json.dumps(message2), encoding='UTF-8')

        # Finalmente enviamos la respuesta
        self._set_headers()
        self.wfile.write(bytes_message)


    def _extract_msg(self):

        # Extraemos el campo content-type de la cabecera que envían
        header = self.headers.get('Content-type')
        ctype, pdict = cgi.parse_header(header)

        # Comprobamos que nos envían un JSON
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            raise Exception()

        # Leemos el JSON y lo metemos en un mapa
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))

        return message


# Poner en marcha el servidor
server_address = ('', 8000)
httpd = socketserver.TCPServer(server_address, Servidor)
print('Starting httpd on port 8000')
httpd.serve_forever()