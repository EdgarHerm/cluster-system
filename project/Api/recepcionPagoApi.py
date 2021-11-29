from flask import Blueprint, jsonify, request
from ..Controller.recepcionPagoController import *

recepcionApi = Blueprint('recepcionApi', __name__, url_prefix='/recpcionPago')

@recepcionApi.route("/mostrar", methods=['POST'])
def buscarPagos():
    estado = "OK"
    mensaje = "Información consultada correctamente"
    
    try:
        print(request.json)
        print("idRecepcionPago" not in request.json)
        
        if "idRecepcionPago" not in request.json or request.json["idRecepcionPago"] == 0:
            print("test")
            recepcions = consultarRecepcion(0)
            if len(recepcions)>0:
                recepcions_json = []
                for x in recepcions:
                    recepcions_json.append({
                        "idColono":x.Colono.idColono,
                        "idRecepcionPago" :x.RecepcionPago.idRecepcionPago,
                        "idListaPago" : x.ListaPago.idListaPago,
                        "nombre": x.Persona.nombre,
                        "apellidos": x.Persona.apellidos,
                        "fechaPago" : x.RecepcionPago.fechaPago,
                        "fotoEvidencia" : x.RecepcionPago.fotEvidencia,
                        "fechaRecepcion" : x.RecepcionPago.fechaRecepcion,
                        "descripcionRecepcion" : x.RecepcionPago.descripcion,
                        "estatus": x.RecepcionPago.estatus,
                        "motivoPago":x.ListaPago.motivoPago,
                        "monto" : x.ListaPago.monto,
                        "descripcionLista": x.ListaPago.descripcion,
                        "fechaInicio": x.ListaPago.fechaInicio,
                        "fechaFin" : x.ListaPago.fechaFin,
                        "estatusLista":x.ListaPago.estatus
                    })
                return jsonify({"Recepcion":recepcions_json})
        else:
            recepcion = consultarRecepcion(request.json["idRecepcionPago"])
            if recepcion is None:
                    return jsonify({
                        "estado" : "ADVERTENCIA",
                        "mensaje": "No se encontro una recepcion de pago con el id especificado"
                    })
            recepcions_json = []
            for x in recepcion:
                recepcions_json.append({
                    "idColono":x.Colono.idColono,
                    "idRecepcionPago" :x.RecepcionPago.idRecepcionPago,
                    "idListaPago" : x.ListaPago.idListaPago,
                    "nombre": x.Persona.nombre,
                    "apellidos": x.Persona.apellidos,
                    "fechaPago" : x.RecepcionPago.fechaPago,
                    "fotoEvidencia" : x.RecepcionPago.fotoEvidencia,
                    "fechaRecepcion" : x.RecepcionPago.fechaRecepcion,
                    "descripcionRecepcion" : x.RecepcionPago.descripcion,
                    "estatus": x.RecepcionPago.estatus,
                    "motivoPago":x.ListaPago.motivoPago,
                    "monto" : x.ListaPago.monto,
                    "descripcionLista": x.ListaPago.descripcion,
                    "fechaInicio": x.ListaPago.fechaInicio,
                    "fechaFin" : x.ListaPago.fechaFin,
                    "estatusLista":x.ListaPago.estatus
                })
            return jsonify({"Recepcion":recepcions_json})
        
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error! Por favor verificalo con un administrador"
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion": str(e)
        })
    

@recepcionApi.route('/agregar', methods=['POST'])
def agregarPagos():
    try:
        if agregarRecepcion(
            request.json["fechaPago"],
            request.json["fotEvidencia"],
            request.json["fechaRecepcion"],
            request.json["descripcion"],  
            request.json["idColono"],
            request.json["idListaPago"]):
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

@recepcionApi.route('/modificar', methods=['POST'])
def modifcarPagos():
    try:
        if "idRecepcionPago" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de pago para modificar"
            })
        if modificarRecepcion(
            request.json["idRecepcionPago"],
            request.json["fechaPago"],
            request.json["fotEvidencia"],
            request.json["descripcion"]):
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


@recepcionApi.route('/cancelar', methods=['POST'])
def cancelarPagos():  
    try: 
        if "idRecepcionPago" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de pago para cancelar"
            }) 
        if cancelarRecepcion(request.json["idRecepcionPago"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Pago cancelado correctamente"
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
        
        
@recepcionApi.route('/aceptar', methods=['POST'])
def aceptarPagos():  
    try: 
        if "idRecepcionPago" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de pago para aceptar"
            }) 
        if aceptarRecepcion(request.json["idRecepcionPago"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Pago acepto correctamente"
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