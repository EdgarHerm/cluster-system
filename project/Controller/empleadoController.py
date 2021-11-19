from ..models import Persona, Usuario, Turno, Empleado
from .turnosController import *
from .personaController import *
from .usuarioController import *
from ..__init__ import db


def consultarEmpleado(idEmpleado):
    if idEmpleado == 0:
        return db.session.query(Empleado, Persona, Usuario, Turno).join(Persona, Persona.idPersona == Empleado.idPersona).join(Usuario, Usuario.idUsuario == Empleado.idUsuario).join(Turno, Turno.idTurno == Empleado.idTurno).filter(Empleado.estatus == 1)

    else:
        return db.session.query(Empleado, Persona, Usuario, Turno).join(Persona, Persona.idPersona == Empleado.idPersona).join(Usuario, Usuario.idUsuario == Empleado.idUsuario).join(Turno, Turno.idTurno == Empleado.idTurno).filter(Empleado.idEmpleado == idEmpleado).filter(Empleado.estatus == 1)


def agregarEmpleado(correo, contraseña, idRol, nombre, apellidos, telefono, estatus, empresa, zona, turno):
    
    persona = insertarPersona(nombre, apellidos, telefono)

    usuario = insertarUsuario(correo, contraseña, idRol, estatus)

    empleado = Empleado(
        empresador=empresa,
        zona=zona,
        estatus=estatus,
        idTurno=turno,
        idPersona=persona,
        idUsuario=usuario
    )
    db.session.add(empleado)
    db.session.commit()
    return True


def modificarEmpleado(idEmpleado, idUsuario, idPersona, correo, contraseña, idRol, nombre, apellidos, telefono, estatus, empresa, zona, turno):
    estatus = 1

    persona = modificarPersona(idPersona, nombre, apellidos, telefono, estatus)

    usuario = modificarUsuario(idUsuario, correo, contraseña, idRol, estatus)

    empleado = db.session.query(Empleado).filter(
        Empleado.idEmpleado == idEmpleado).first()
    empleado.empresador = empresa
    empleado.zona = zona
    empleado.estatus = estatus
    empleado.idTurno = turno
    empleado.idPersona = persona
    empleado.idUsuario = usuario

    db.session.add(empleado)
    db.session.commit()

    return True


def desactivarEmpleado(idEmpleado):

    empleado = db.session.query(Empleado).filter(
        Empleado.idEmpleado == idEmpleado).first()
    empleado.estatus = 0
    db.session.add(empleado)
    db.session.commit()

    return True


def activarEmpleado(idEmpleado):

    empleado = db.session.query(Empleado).filter(
        Empleado.idEmpleado == idEmpleado).first()
    empleado.estatus = 1
    db.session.add(empleado)
    db.session.commit()

    return True
