import json
from flask import Blueprint, jsonify, request
from ..Controller.usuarioController import *
from ..Controller.colonoController import *

sesionApi = Blueprint('sesionApi', __name__, url_prefix='/sesion')


@sesionApi.route('/login', methods=['POST'])
def iniciarSesion():
    try:

        if "usuario" not in request.json and "contrasenia" not in request.json:

            return jsonify({
                "estado": "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un usuario y contraseña"
            })

        if request.json["usuario"] and request.json["contrasenia"]:
            
            sesion = login(request.json["usuario"],
                           request.json["contrasenia"])
            
            colono = consultarColonoToken(sesion)
            if (colono):
    
                colonos_json = []
                for x in colono:
                    colonos_json.append({
                        "Colono": {
                            "idColono": x.Colono.idColono,
                            "idPersona": x.Colono.idPersona,
                            "idUsuario": x.Colono.idUsuario,
                            "idDomicilio": x.Colono.idDomicilio,
                            "foto": x.Colono.fotografia,
                            "estatus": x.Colono.estatus,
                        }, "Persona": {
                            "nombre": x.Persona.nombre,
                            "apellidos": x.Persona.apellidos,
                            "telefono": x.Persona.telefono,
                        }, "Usuario": {
                            "correo": x.Usuario.correo,
                            "constraseña": x.Usuario.contraseña,
                        }, "Domicilio": {
                            "calle": x.Domicilio.calle,
                            "numero": x.Domicilio.numero,
                            "descripcion": x.Domicilio.descripcion
                        }
                    })
                    
            if sesion is None:
                return jsonify({
                        "estado" : "ADVERTENCIA",
                        "mensaje": "No se encontro una usuario o contraseña para ingresar"
                    })
            return jsonify({"result":sesion,
                            "colono":colonos_json})
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al iniciar sesion! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado": estado,
                "mensaje": mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al iniciar sesion! Por favor verificalo con un administrador o revisa tu solicitud"

        return jsonify({
            "estado": estado,
            "mensaje": mensaje,
            "excepcion": str(e)
        })


@sesionApi.route('/logout', methods=['POST'])
def salirSesion():
    try:

        if "token" not in request.json :
            return jsonify({
                "estado": "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un token"
            })

        if logout(request.json["token"]):
            return jsonify({
            "estado" : "OK",
            "mensaje": "sesion cerrada correctamente"
        }) 
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al cerrar sesion! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al cerrar sesion! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })
        
