import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('name: ' + p['name'])
        print('apellidos: ' + p['apellidos'])
        print('Nombre_maquina: ' + p['Nombre_maquina'])
        print('IP:' + p['IP'])
        print('')
