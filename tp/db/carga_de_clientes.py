import json
from tp.models.clientes import Clientes


def cargar_clientes():
    clientes = []

    with open('src/db/clientes_mock.json', 'r') as file:
        clientes_json = json.load(file)
        for cliente in clientes_json:
            clientes.append(
                Clientes
                (cliente['nombre_completo'],
                cliente['edad'],
                 cliente['dni'])
            )
    return clientes