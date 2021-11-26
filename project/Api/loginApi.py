import json
from flask import Blueprint, jsonify, request
from ..Controller.usuarioController import *
from ..Controller.colonoController import *
from ..Controller.empleadoController import *

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
            usuarios_json = []

            sesion = login(request.json["usuario"],
                           request.json["contrasenia"])
            
            token = consultarUsuario(sesion)
            if token.idRol == 3:
                colono = consultarColonoToken(sesion)
                if (colono):

                    
                    for x in colono:
                        usuarios_json.append({

                            "idColono": x.Colono.idColono,
                            "idPersona": x.Colono.idPersona,
                            "idUsuario": x.Colono.idUsuario,
                            "idDomicilio": x.Colono.idDomicilio,
                            "idRol": x.Usuario.idRol,
                            "foto": x.Colono.fotografia,
                            "estatus": x.Colono.estatus,

                            "nombre": x.Persona.nombre,
                            "apellidos": x.Persona.apellidos,
                            "telefono": x.Persona.telefono,

                            "correo": x.Usuario.correo,
                            "constraseña": x.Usuario.contraseña,
                            "rol": x.Rol.nombre,


                            "calle": x.Domicilio.calle,
                            "numero": x.Domicilio.numero,
                            "descripcion": x.Domicilio.descripcion,
                            "token": sesion

                        })
            elif token.idRol !=3:
                empleados = consultarEmpleadoToken (sesion)
                if empleados:
                    for x in empleados:
                        usuarios_json.append({
                            "idEmpleado": x.Empleado.idEmpleado,
                            "idPersona": x.Empleado.idPersona,
                            "idUsuario": x.Empleado.idUsuario,
                            "idTurno": x.Empleado.idTurno,
                            "idRol":x.Usuario.idRol,
                            "empresa": x.Empleado.empresador,
                            "zona": x.Empleado.zona,
                            "estatus": x.Empleado.estatus,
                            "nombre": x.Persona.nombre,
                            "apellidos": x.Persona.apellidos,
                            "telefono": x.Persona.telefono,
                            "correo": x.Usuario.correo,
                            "rol": x.Rol.nombre,
                            "constraseña": x.Usuario.contraseña,
                            "horaInicio": x.Turno.horaInicio,
                            "horaFin": x.Turno.horaFin,
                            "token": sesion
                    })
                    

            if sesion is None:
                return jsonify({
                    "estado": "ADVERTENCIA",
                    "mensaje": "No se encontro una usuario o contraseña para ingresar"
                })
            return jsonify({
                "colono": usuarios_json})
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

        if "token" not in request.json:
            return jsonify({
                "estado": "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un token"
            })

        if logout(request.json["token"]):
            return jsonify({
                "estado": "OK",
                "mensaje": "sesion cerrada correctamente"
            })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al cerrar sesion! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado": estado,
                "mensaje": mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al cerrar sesion! Por favor verificalo con un administrador o revisa tu solicitud"

        return jsonify({
            "estado": estado,
            "mensaje": mensaje,
            "excepcion": str(e)
        })
