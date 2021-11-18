import json 
from flask import Blueprint, jsonify, request
from ..Controller.vehiculosController import *

vehiculoApi = Blueprint('vehiculoApi', __name__, url_prefix='/vehiculo')


@vehiculoApi.route("/mostrar", methods=['POST'])
def buscarVehiculos():
    estado = "OK"
    mensaje = "Información consultada correctamente"
    
    try:
        print(request.json)
        print("idColono" not in request.json)
        
        if "idColono" not in request.json or request.json["idColono"] == 0:
            print("test")
            vehiculos = consultarVehiculo(0)
            if len(vehiculos)>0:
                Vehiculos_json = []
                for vehiculo in vehiculos:
                    vehiculo_dictionary = vehiculo.__dict__
                    del vehiculo_dictionary['_sa_instance_state']
                    Vehiculos_json.append(vehiculo_dictionary)
                return jsonify(Vehiculos_json)
        else:
            vehiculo = consultarVehiculo(request.json["idColono"])
            if vehiculo is None:
                    return jsonify({
                        "estado" : "ADVERTENCIA",
                        "mensaje": "No se encontro un vehiculo con el id especificado"
                    })
            vehiculo_dictionary = vehiculo.__dict__
            del vehiculo_dictionary['_sa_instance_state']
            return jsonify(vehiculo_dictionary)
        
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error! Por favor verificalo con un administrador"
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion": str(e)
        })
        
@vehiculoApi.route('/agregar', methods=['POST'])
def agregarVehiculos():
    try:
        if agregarVehiculo(
            request.json["marca"],
            request.json["modelo"],
            request.json["color"],
            request.json["matricula"],  
            request.json["fotografia"],
            request.json["estatus"],
            request.json["idColono"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Vehiculo registrado correctamente"
            })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al agregar el registro! Por favor verificalo con un administrador o revisa tu solicitud"    
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al agregar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })

@vehiculoApi.route('/modificar', methods=['POST'])
def modificarVehiculos():
    try: 
        if "idVehiculo" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de vehiculo para modificar"
            })
        if modificarVehiculo(
            request.json["idVehiculo"],
            request.json["marca"],
            request.json["modelo"],
            request.json["color"],
            request.json["matricula"],  
            request.json["fotografia"],
            request.json["estatus"],
            request.json["idColono"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Vehiculo modificado correctamente"
            })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al modificar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al modificar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })
        
        #cambia del estatus de activo a incativo del Ingrediente
@vehiculoApi.route('/eliminar', methods=['POST'])
def eliminarVehiculos():  
    try: 
        if "idVehiculo" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para eliminar"
            }) 
        if eliminarVehiculos(request.json["idVehiculo"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Vehiculo eliminado correctamente"
            }) 
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al eliminar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al modificar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })