import requests
import json
from flask import Flask, jsonify, request

from models.contacto import Contacto
from models.reservas import Reserva, generador_nro_reserva
from models.clientes import Clientes

from db.carga_de_clientes import cargar_clientes
from db.carga_de_habitaciones import cargar_habitaciones
from db.carga_de_recreaciones import cargar_recreaciones
from db.carga_de_reservas import cargar_reservas

app = Flask(__name__)

clientes = cargar_clientes()
habitaciones = cargar_habitaciones()
recreaciones = cargar_recreaciones()
reservas = cargar_reservas()
# tipo_habitaciones = ["Simple", "Doble", "Cuádruple", "Premium", "Suite"]


@app.route('/api/hotel/informacion', methods=['GET'])
def informacion():
    return jsonify(Contacto().serialize())


@app.route('/api/hotel/habitaciones', methods=['GET'])
def ver_habitaciones():
    tipo_habitaciones = []
    with open("tp/db/habitaciones_mock.json","r") as mock_habitaciones:
        archivo = json.load(mock_habitaciones)
        for i in archivo:
            if not i["tipo"] in tipo_habitaciones:
                tipo_habitaciones.append(i["tipo"])
    diccionario = {
        "habitaciones disponibles" : tipo_habitaciones
    }
    return jsonify(diccionario)


@app.route('/api/hotel/habitaciones/<habitacion>', methods=['GET'])
def ver_habitacion(habitacion):
    for room in habitaciones:
        if room.tipo == habitacion:
            return jsonify(room.serialize())

    return jsonify({'status': 'not found'})


@app.route('/api/hotel/recreaciones', methods=['GET'])
def ver_recreaciones():
    return jsonify([actividad.serialize() for actividad in recreaciones])

#otro get privado para ver todas las reservas


@app.route('/api/hotel/reservar', methods=['POST'])
def crear_reserva():
    reserva = request.json

    try:
        nueva_reserva = Reserva(
            generador_nro_reserva(),
            reserva['tipo_habitacion'],
            reserva['cantidad_huespedes'],
            reserva['fecha_entrada'],
            reserva['fecha_salida'],
         )
        #request.args("dni")

        reserva.append(nueva_reserva)

    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code="ERROR_BAD",
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(nueva_reserva.serialize())

#relacionar reservas con clientes, con el dni, request args?

"""
@app.route('/api/hotel/reservar', methods=['POST'])
def crear_reserva():
    reserva = request.json
    numero_reserva = generador_nro_reserva()
    tipo_habitacion = reserva["tipo_habitacion"]
    cantidad_huespedes = reserva["cantidad_huespedes"]
    fecha_entrada = reserva["fecha_entrada"]
    fecha_salida = reserva["fecha_salida"]
    reserva_creada = {"numero_reserva": numero_reserva, "tipo_habitacion": tipo_habitacion,
                      "cantidad_huespedes": cantidad_huespedes, "fecha_entrada": fecha_entrada,
                      "fecha_salida": fecha_salida}

    return jsonify({"reserva": reserva_creada, "status":"ok"})
"""

@app.route('/api/hotel/clientes', methods=['POST'])
def crear_cliente():
    cliente = request.json

    try:
        nuevo_cliente = Clientes(
           cliente['nombre_completo'],
           cliente['edad'],
           cliente['dni'],
         )

        cliente.append(nuevo_cliente)

    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code="ERROR_BAD",
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(nuevo_cliente.serialize())


@app.route('/api/hotel/clientes/<dni>', methods=['PUT'])
def modificar_cliente(dni):
    body = request.json
    nombre = body['nombre_completo']
    edad = body["edad"]
    nro_dni = body["dni"]
    for indice, c in enumerate(clientes):
        if c['dni'] == dni:
           return jsonify({'Cliente':{"nombre_completo": nombre, "edad": edad, "dni": nro_dni},
                           'busqueda': dni, "status":"ok"})

    return jsonify({'busqueda': dni,
                    'status':'not found'})
#???? ayuda con los puts


@app.route('/api/hotel/reservas/<nro_reserva>', methods=['PUT'])
def modificar_reserva(nro_reserva):
    body = request.json
    numero_reserva = body["numero_reserva"]
    tipo_habitacion = body["tipo_habitacion"]
    cantidad_huespedes = body["cantidad_huespedes"]
    fecha_entrada = body["fecha_entrada"]
    fecha_salida = body["fecha_salida"]
    for indice, r in enumerate(reservas): #el indice hay q usarlo?
        if r['numero_reserva'] == nro_reserva:
           return jsonify({'Reserva':{"numero_reserva": numero_reserva, "tipo_habitacion": tipo_habitacion,
                                      "cantidad_huespedes": cantidad_huespedes, "fecha_entrada": fecha_entrada,
                                      "fecha_salida": fecha_salida},
                           'busqueda': nro_reserva, "status":"ok"})

    return jsonify({'busqueda': nro_reserva,
                    'status':'not found'})


@app.route('/api/hotel/reservas/<nro_reserva>', methods=['DELETE'])
def eliminar_reserva(nro_reserva):
    for indice, r in reservas:
        if r['numero_reserva'] == nro_reserva:
            reservas[indice:indice+1] = []
            return jsonify({'Reserva': r, 'busqueda': nro_reserva, 'status':'ok'})
    return jsonify({'productos': nro_reserva, 'status':'not found'})


@app.route('/api/hotel/clientes/<dni>', methods=['DELETE'])
def eliminar_cliente(dni):
    for indice, c in clientes:
        if c['dni'] == dni:
            clientes[indice:indice+1] = []
            return jsonify({'Cliente': c, 'busqueda': dni, 'status':'ok'})
    return jsonify({'busqueda': dni, 'status':'not found'})

#de terceros
@app.route("/api/hotel/clima", methods=["GET"])
def pronostico_clima():

    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q":"Antananarivo", "days":"14"}
    headers = {
	    "X-RapidAPI-Key": "3ee5845b4cmsh27d978b5dfc3090p119f03jsn40de6a1152b7",
	    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"}

    response = requests.get(url, headers=headers, params=querystring)

    return print(response.json())


if __name__ == '__main__':
    app.run(debug=True, port=6000)

