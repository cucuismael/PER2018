import http.server
import socketserver
import json

PORT = 8000

# Conectarse con el servidor
conn = http.client.HTTPConnection('212.128.255.156', PORT)
print (conn)
# -- Enviar un mensaje de solicitud (Verbo: GET), Recurso: Raiz
path= input()
conn.request("GET","/" + path)

# -- Leer el mensaje de respuesta recibido del servidor
r1 = conn.getresponse()
print (r1)
# -- Imprimir la linea de estado de la respuesta
print(r1.status, r1.reason)

# -- Leer el contenido de la respuesta y converirlo a una cadena
data1 = r1.read().decode("utf-8")
if "json" in path:
    with open(path + ".txt") as json_file:
        data = json.load(json_file)
        for p in data['people']:
            print('name: ' + p['name'])
            print('apellidos: ' + p['apellidos'])
            print('Nombre_maquina: ' + p['Nombre_maquina'])
            print('IP:' + p['IP'])
            print('')
# -- Imprimir el fichero html recibido
else:
    print(data1)
