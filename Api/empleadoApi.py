import json
from json import JSONEncoder
from flask import Blueprint, jsonify, request
from Controller.empleadoController import *

empleadoApi = Blueprint('empleadoApi', __name__, url_prefix="/empleado")


@empleadoApi.route('/mostrar', methods=['POST'])
def mostrarEmpleado():
    estado = "OK"
    mensaje = "Información consultada correctamente"

    try:
        print(request.json)
        print("idEmpleado" not in request.json)

        if "idEmpleado" not in request.json or request.json["idEmpleado"] == 0:
            print("test")
            empleados = consultarEmpleado(0)
            if (empleados):

                empleados_json = []
                for x in empleados:
                    empleados_json.append({
                        "Empleado": {
                            "idEmpleado": x.Empleado.idEmpleado,
                            "idPersona": x.Empleado.idPersona,
                            "idUsuario": x.Empleado.idUsuario,
                            "idTurno": x.Empleado.idTurno,
                            "empresa": x.Empleado.empresador,
                            "zona": x.Empleado.zona,
                            "estatus": x.Empleado.estatus,
                        }, "Persona": {
                            "nombre": x.Persona.nombre,
                            "apellidos": x.Persona.apellidos,
                            "telefono": x.Persona.telefono,
                        }, "Usuario": {
                            "correo": x.Usuario.correo,
                            "constraseña": x.Usuario.contraseña,
                        }, "Turno": {
                            "horaInicio": x.Turno.horaInicio,
                            "horaFin": x.Turno.horaFin,
                        }
                    })
                return jsonify(empleados_json)
        else:
            empleado = consultarEmpleado(request.json["idEmpleado"])
            if empleado is None:
                return jsonify({
                    "estado": "ADVERTENCIA",
                    "mensaje": "No se encontro un Empleado con el id especificado"
                })
            empleados_json = []
            for x in empleado:
                empleados_json.append({
                    "Empleado": {
                        "idEmpleado": x.Empleado.idEmpleado,
                        "idPersona": x.Empleado.idPersona,
                        "idUsuario": x.Empleado.idUsuario,
                        "idTurno": x.Empleado.idTurno,
                        "empresa": x.Empleado.empresador,
                        "zona": x.Empleado.zona,
                        "estatus": x.Empleado.estatus,
                    }, "Persona": {
                        "nombre": x.Persona.nombre,
                        "apellidos": x.Persona.apellidos,
                        "telefono": x.Persona.telefono,
                    }, "Usuario": {
                        "correo": x.Usuario.correo,
                        "constraseña": x.Usuario.contraseña,
                    }, "Turno": {
                        "horaInicio": x.Turno.horaInicio,
                        "horaFin": x.Turno.horaFin,
                    }
                })
            return jsonify(empleados_json)

    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error! Por favor verificalo con un administrador"
        return jsonify({
            "estado": estado,
            "mensaje": mensaje,
            "excepcion": str(e)
        })


@empleadoApi.route('/agregar', methods=['POST'])
def agregarEmpleados():
    try:
        if agregarEmpleado(

            request.json["correo"],
            request.json["contraseña"],
            request.json["idRol"],
            request.json["nombre"],
            request.json["apellidos"],
            request.json["telefono"],
            request.json["estatus"],
            request.json["empresa"],
            request.json["zona"],
            request.json["turno"]
        ):
            return jsonify({
                "estado": "OK",
                "mensaje": "Empleado registrado correctamente"
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


@empleadoApi.route('/modificar', methods=['POST'])
def modificarEmpleados():
    try:
        if "idEmpleado" not in request.json and "idUsuario" not in request.json and "idPersona" not in request.json:
            return jsonify({
                "estado": "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id para modificar"
            })
        if modificarEmpleado(
            request.json["idEmpleado"],
            request.json["idUsuario"],
            request.json["idPersona"],
            request.json["correo"],
            request.json["contraseña"],
            request.json["idRol"],
            request.json["nombre"],
            request.json["apellidos"],
            request.json["telefono"],
            request.json["estatus"],
            request.json["empresa"],
            request.json["zona"],
            request.json["turno"]
        ):
            return jsonify({
                "estado": "OK",
                "mensaje": "Empleado modificado correctamente"
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


@empleadoApi.route('/desactivar', methods=['POST'])
def desactivarEmpleados():
    try:
        if "idEmpleado" not in request.json:
            return jsonify({
                "estado": "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de Empleado para desactivar"
            })
        if desactivarEmpleado(request.json["idEmpleado"]):
            return jsonify({
                "estado": "OK",
                "mensaje": "Empleado desactivado correctamente"
            })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al desactivar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
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


@empleadoApi.route('/activar', methods=['POST'])
def activarEmpleados():
    try:
        if "idEmpleado" not in request.json:
            return jsonify({
                "estado": "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de Empleado para activar"
            })
        if activarEmpleado(request.json["idEmpleado"]):
            return jsonify({
                "estado": "OK",
                "mensaje": "Empleado activado correctamente"
            })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al activar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
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
