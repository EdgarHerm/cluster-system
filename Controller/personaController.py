from ..models import Persona
from ..__init__ import dbSQL


def consultarPersona(idPersona):
    if idPersona == 0:
        return Persona.query.all()
    else:
        return dbSQL.session.query(Persona).filter(Persona.idPersona == idPersona).first()


def insertarPersona(nombre, apellidos, telefono):
    agregarPersona = Persona(
        nombre=nombre,
        apellidos=apellidos,
        telefono=telefono
    )

    dbSQL.session.add(agregarPersona)
    dbSQL.session.flush()
    return agregarPersona.idPersona


def modificarPersona(idPersona, nombre, apellidos, telefono,estatus):

    modificarPersona = dbSQL.session.query(Persona).filter(Persona.idPersona == idPersona).first()
    modificarPersona.nombre = nombre
    modificarPersona.apellidos = apellidos
    modificarPersona.telefono = telefono
    modificarPersona.estatus = estatus

    dbSQL.session.add(modificarPersona)
    dbSQL.session.flush()

    return modificarPersona.idPersona

def eliminarPersona(idPersona):
    eliminarPersonas = dbSQL.session.query(Persona).filter(Persona.idPersona == idPersona).first()
    dbSQL.session.delete(eliminarPersonas)
    dbSQL.session.commit()
    return True