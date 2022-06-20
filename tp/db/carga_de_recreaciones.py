import json
from tp.models.recreaciones import Recreaciones


def cargar_recreaciones():
   recreaciones = []

   with open('src/db/recreaciones_mock.json', 'r') as file:
       recreaciones_json = json.load(file)
       for recreacion in recreaciones_json:
            recreaciones.append(
                Recreaciones(
                    recreacion['nombre'],
                    recreacion['horario'],
                    recreacion['precio'],
                    recreacion['disponibilidad']
                )
            )
   return recreaciones

