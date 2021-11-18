from flask import Blueprint, jsonify, request
from Controller.domicilioController import *

domicilioApi = Blueprint('domicilioApi', __name__,url_prefix='/domicilio')

@domicilioApi.route("/mostrar", methods=['POST'])
def buscarDomicilios():
    estado = "OK"
    mensaje = "Información consultada correctamente"
    
    try:
        print(request.json)
        print("idDomicilio" not in request.json)
        
        if "idDomicilio" not in request.json or request.json["idDomicilio"] == 0:
            print("test")
            Domicilios = consultarDomicilio(0)
            if len(Domicilios)>0:
                Domicilios_json = []
                for Domicilio in Domicilios:
                    Domicilio_dictionary = Domicilio.__dict__
                    del Domicilio_dictionary['_sa_instance_state']
                    Domicilios_json.append(Domicilio_dictionary)
                return jsonify(Domicilios_json)
        else:
            Domicilio = consultarDomicilio(request.json["idDomicilio"])
            if Domicilio is None:
                    return jsonify({
                        "estado" : "ADVERTENCIA",
                        "mensaje": "No se encontro una lista de domicilio con el id especificado"
                    })
            Domicilio_dictionary = Domicilio.__dict__
            del Domicilio_dictionary['_sa_instance_state']
            return jsonify(Domicilio_dictionary)
        
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error! Por favor verificalo con un administrador"
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion": str(e)
        })
        
@domicilioApi.route('/agregar', methods=['POST'])
def agregarDomicilios(): 
    try:
        if agregarDomicilio(
            request.json["calle"],
            request.json["numero"],
            request.json["descripcion"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Domicilio registrado correctamente"
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
        
@domicilioApi.route('/modificar', methods=['POST'])
def modificarDomicilios():
    try: 
        if "idDomicilio" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de domicilio para modificar"
            })
        if modificarDomicilio(
            request.json["idDomicilio"],
             request.json["calle"],
            request.json["numero"],
            request.json["descripcion"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Domicilio modificado correctamente"
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
        
@domicilioApi.route('/desactivar', methods=['POST'])
def desactivarDomicilios():  
    try: 
        if "idDomicilio" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de domicilio para eliminar"
            }) 
        if desactivarDomicilio(request.json["idDomicilio"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Domicilio desactivado correctamente"
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
        
@domicilioApi.route('/activar', methods=['POST'])
def activarDomicilios():  
    try: 
        if "idDomicilio" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de domicilio para eliminar"
            }) 
        if activarDomicilio(request.json["idDomicilio"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Domicilio desactivado correctamente"
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
        
        