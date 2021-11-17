from flask import Blueprint, jsonify, request
from ..Controller.listaPagoController import *

listaPagoApi = Blueprint('listaPagoApi', __name__,url_prefix='/listaPago')

@listaPagoApi.route("/mostrar", methods=['POST'])
def buscarListaPagos():
    estado = "OK"
    mensaje = "Información consultada correctamente"
    
    try:
        print(request.json)
        print("idListaPago" not in request.json)
        
        if "idListaPago" not in request.json or request.json["idListaPago"] == 0:
            print("test")
            listaPagos = consultarListaPago(0)
            if len(listaPagos)>0:
                listaPagos_json = []
                for listaPago in listaPagos:
                    listaPago_dictionary = listaPago.__dict__
                    del listaPago_dictionary['_sa_instance_state']
                    listaPagos_json.append(listaPago_dictionary)
                return jsonify(listaPagos_json)
        else:
            listaPago = consultarListaPago(request.json["idListaPago"])
            if listaPago is None:
                    return jsonify({
                        "estado" : "ADVERTENCIA",
                        "mensaje": "No se encontro una lista de pago con el id especificado"
                    })
            listaPago_dictionary = listaPago.__dict__
            del listaPago_dictionary['_sa_instance_state']
            return jsonify(listaPago_dictionary)
        
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error! Por favor verificalo con un administrador"
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion": str(e)
        })

@listaPagoApi.route('/agregar', methods=['POST'])
def agregarListaPagos(): 
    try:
        if agregarListaPago(
            request.json["motivoPago"],
            request.json["monto"],
            request.json["descripcion"],
            request.json["fechaFin"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Pago registrado correctamente"
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
        

@listaPagoApi.route('/modificar', methods=['POST'])
def modificarListaPagos():
    try: 
        if "idListaPago" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de pago para modificar"
            })
        if modificarListaPago(
            request.json["idListaPago"],
            request.json["motivoPago"],
            request.json["monto"],
            request.json["descripcion"],
            request.json["fechaFin"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Pago modificado correctamente"
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

@listaPagoApi.route('/desactivar', methods=['POST'])
def desactivarPagos():  
    try: 
        if "idListaPago" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de pago para eliminar"
            }) 
        if desactivarListaPago(request.json["idListaPago"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Pago desactivado correctamente"
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
        
@listaPagoApi.route('/desactivar', methods=['POST'])
def activarPagos():  
    try: 
        if "idListaPago" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de pago para eliminar"
            }) 
        if activarListaPago(request.json["idListaPago"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Pago activado correctamente"
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