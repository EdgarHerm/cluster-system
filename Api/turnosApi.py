import json 
from flask import Blueprint, jsonify, request
from ..Controller.turnosController import *

turnoApi = Blueprint('turnoApi', __name__, url_prefix='/turno')


@turnoApi.route("/mostrar", methods=['GET'])
def consultarTurnos():
    turnos = consultarTurno()
    turnos_json = []
    for turno in turnos:
        turnos_dictionary = turno.__dict__
        del turnos_dictionary['_sa_instance_state']
        turnos_json.append(turnos_dictionary)
    return jsonify(turnos_json)

        
@turnoApi.route('/agregar', methods=['POST'])
def agregarTurnos():
    try:
        if agregarTurno(
            request.json["horaInicio"],
            request.json["horaFin"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Turno registrado correctamente"
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

@turnoApi.route('/modificar', methods=['POST'])
def modificarTurnos():
    try: 
        if "idTurno" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de Turno para modificar"
            })
        if modificarTurno(
            request.json["idTurno"],
            request.json["horaInicio"],
            request.json["horaFin"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Turno modificado correctamente"
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
        
@turnoApi.route('/desactivar', methods=['POST'])
def desactivarTurnos():  
    try: 
        if "idTurno" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de turno para eliminar"
            }) 
        if desactivarTurno(request.json["idTurno"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Turno eliminado correctamente"
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
        
@turnoApi.route('/activar', methods=['POST'])
def sactivarTurnos():  
    try: 
        if "idTurno" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de turno para eliminar"
            }) 
        if activarTurno(request.json["idTurno"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Turno eliminado correctamente"
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