import json 
from flask import Blueprint, jsonify, request
from Controller import vehiculosController

vehiculos = Blueprint('vehiculos', __name__, url_prefix='/vehiculos')

def consultarVehiculo(usuario_actual):
    vehiculos = vehiculosController.consultarVehiculo()
    vehiculos_json = []
    for ingrediente in vehiculos:
        ingredientes_dictionary = ingrediente.__dict__
        del ingredientes_dictionary['_sa_instance_state']
        vehiculos_json.append(ingredientes_dictionary)
    return jsonify(vehiculos_json)

