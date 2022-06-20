import json
from tp.models.habitaciones import Habitaciones


def cargar_habitaciones():
    habitaciones = []

    with open('src/db/habitaciones_mock.json', 'r') as file:
        habitaciones_json = json.load(file)
        for habitacion in habitaciones_json:
            habitaciones.append(
                Habitaciones(
                    habitacion['tipo'],
                    habitacion['cantidad_de_huespedes'],
                    habitacion['precio']
                )
            )
    return habitaciones

#como incluir las clases hijas?