import json
from json import JSONEncoder
from flask import Blueprint, jsonify, request
from ..Controller.colonoController import *

colonoApi = Blueprint('colonoApi', __name__, url_prefix='/colono')


def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4)


@colonoApi.route("/mostrar", methods=['POST'])
def buscarColonos():

    estado = "OK"
    mensaje = "Información consultada correctamente"

    try:
        print(request.json)
        print("idColono" not in request.json)

        if "idColono" not in request.json or request.json["idColono"] == 0:
            print("test")
            colonos = consultarColono(0)
            if (colonos):

                colonos_json = []
                for x in colonos:
                    colonos_json.append({
                            "idColono": x.Colono.idColono,
                            "idPersona": x.Colono.idPersona,
                            "idUsuario": x.Colono.idUsuario,
                            "idDomicilio": x.Colono.idDomicilio,
                            "foto": x.Colono.fotografia,
                            "estatus": x.Colono.estatus,
                            "nombre": x.Persona.nombre,
                            "apellidos": x.Persona.apellidos,
                            "telefono": x.Persona.telefono,
                            "correo": x.Usuario.correo,
                            "constraseña": x.Usuario.contraseña,
                            "calle": x.Domicilio.calle,
                            "numero": x.Domicilio.numero,
                            "descripcion": x.Domicilio.descripcion
                        }
                    )
                return jsonify({"colono":colonos_json})
        else:
            colono = consultarColono(request.json["idColono"])
            if colono is None:
                return jsonify({
                    "estado": "ADVERTENCIA",
                    "mensaje": "No se encontro un colono con el id especificado"
                })
            colonos_json = []
            for x in colono:
                colonos_json.append({
                        "idColono": x.Colono.idColono,
                        "idPersona": x.Colono.idPersona,
                        "idUsuario": x.Colono.idUsuario,
                        "idDomicilio": x.Colono.idDomicilio,
                        "foto": x.Colono.fotografia,
                        "estatus": x.Colono.estatus,
                        "nombre": x.Persona.nombre,
                        "apellidos": x.Persona.apellidos,
                        "telefono": x.Persona.telefono,
                        "correo": x.Usuario.correo,
                        "constraseña": x.Usuario.contraseña,
                        "calle": x.Domicilio.calle,
                        "numero": x.Domicilio.numero,
                        "descripcion": x.Domicilio.descripcion
                    
                })
            return jsonify({"colono":colonos_json})

    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error! Por favor verificalo con un administrador"
        return jsonify({
            "estado": estado,
            "mensaje": mensaje,
            "excepcion": str(e)
        })


@colonoApi.route('/agregar', methods=['POST'])
def agregarcolonos():
    try:
        if agregarColono(
            request.json["fotografia"],
            request.json["correo"],
            request.json["contraseña"],
            request.json["idRol"],
            request.json["nombre"],
            request.json["apellidos"],
            request.json["telefono"],
            request.json["idDomicilio"]
        ):
            return jsonify({
                "estado": "OK",
                "mensaje": "Colono registrado correctamente"
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

@colonoApi.route('/modificar', methods=['POST'])
def modificarColonos():
    try:
        if "idColono" not in request.json and "idUsuario" not in request.json and "idPersona" not in request.json: 
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de vehiculo para modificar"
            })
        if modificarColono(
            request.json["idColono"],
            request.json["idUsuario"],
            request.json["idPersona"],
            request.json["idDomicilio"],
            request.json["fotografia"],
            request.json["correo"],
            request.json["contraseña"],
            request.json["idRol"],
            request.json["nombre"],
            request.json["apellidos"],
            request.json["telefono"]
        ):
            return jsonify({
                "estado": "OK",
                "mensaje": "Colono registrado correctamente"
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
@colonoApi.route('/desactivar', methods=['POST'])
def desactivarColonos():  
    try: 
        if "idColono" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de colono para desactivar"
            }) 
        if desactivarColono(request.json["idColono"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Colono desactivado correctamente"
            }) 
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al desactivar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
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
        
@colonoApi.route('/activar', methods=['POST'])
def activarColonos():  
    try: 
        if "idColono" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de colono para activar"
            }) 
        if activarColono(request.json["idColono"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Colono activado correctamente"
            }) 
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al activar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
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