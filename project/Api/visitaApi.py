from flask import Blueprint, jsonify, request
from ..Controller.visitaController import *

visitaApi = Blueprint('visitaApi', __name__, url_prefix='/visita')


@visitaApi.route("/mostrar", methods=['POST'])
def buscarVisita():
    estado = "OK"
    mensaje = "Información consultada correctamente"
    
    try:
        print(request.json)
        print("idVisita" not in request.json)
        
        if "idVisita" not in request.json or request.json["idVisita"] == 0:
            print("test")
            visitas = consultarVisitas(0)
            if len(visitas)>0:
                Visitas_json = []
                for visita in visitas:
                    visitas_dictionary = visita.__dict__
                    del visitas_dictionary['_sa_instance_state']
                    Visitas_json.append(visitas_dictionary)
                return jsonify(Visitas_json)
        else:
            visita = consultarVisitas(request.json["idVisita"])
            if visita is None:
                    return jsonify({
                        "estado" : "ADVERTENCIA",
                        "mensaje": "No se encontro un visita con el id especificado"
                    })
            visitas_dictionary = visita.__dict__
            del visitas_dictionary['_sa_instance_state']
            return jsonify(visitas_dictionary)
        
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error! Por favor verificalo con un administrador"
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion": str(e)
        })


@visitaApi.route('/agregar', methods=['POST'])
def agregarVisita():
    try:
        if agregarVisitas(
                request.json["nombre"],
                request.json["matricula"],
                request.json["modelo"],
                request.json["color"],
                request.json["idColono"]):
            return jsonify({
                "estado": "OK",
                "mensaje": "Visita registrada correctamente"
            })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al agregar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado": estado,
                "mensaje": mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al agregar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
        return jsonify({
            "estado": estado,
            "mensaje": mensaje,
            "excepcion": str(e)
        })


@visitaApi.route('/modificar', methods=['POST'])
def modificarVisitas():
    try:
        if "idVisita" not in request.json:
            return jsonify({
                "estado": "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de visita para modificar"
            })
        if modificarVisita(
            request.json["idVisita"],
            request.json["nombre"],
            request.json["matricula"],
            request.json["modelo"],
            request.json["color"]):
            return jsonify({
                "estado": "OK",
                "mensaje": "Visita modificada correctamente"
            })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al modificar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado": estado,
                "mensaje": mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al modificar el registro! Por favor verificalo con un administrador o revisa tu solicitud"

        return jsonify({
            "estado": estado,
            "mensaje": mensaje,
            "excepcion": str(e)
        })

@visitaApi.route('/entradaVisita', methods=['POST'])
def entradaVisitas():  
    try: 
        if "idVisita" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de visita para la entrada de visita"
            }) 
        if entradaVisita(request.json["idVisita"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Entrada registrada correctamente"
            }) 
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al modificar la endtada del registro! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al modificar la endtada del registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })

@visitaApi.route('/salidaVisita', methods=['POST'])
def salidaVisitas():  
    try: 
        if "idVisita" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de visita para la salida de visita"
            }) 
        if salidaVisita(request.json["idVisita"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Salida registrada correctamente"
            }) 
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al modificar la endtada del registro! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al modificar la endtada del registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })

@visitaApi.route('/cancelarVisita', methods=['POST'])
def cancelarVisitas():  
    try: 
        if "idVisita" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de visita para cancelar una visita"
            }) 
        if cancelarVisita(request.json["idVisita"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Visita cancelada correctamente"
            }) 
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al modificar la endtada del registro! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al modificar la endtada del registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })