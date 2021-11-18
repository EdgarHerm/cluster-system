from ..models import Persona
from ..__init__ import db


def consultarPersona(idPersona):
    if idPersona == 0:
        return Persona.query.all()
    else:
        return db.session.query(Persona).filter(Persona.idPersona == idPersona).first()


def insertarPersona(nombre, apellidos, telefono):
    agregarPersona = Persona(
        nombre=nombre,
        apellidos=apellidos,
        telefono=telefono
    )

    db.session.add(agregarPersona)
    db.session.flush()
    return agregarPersona.idPersona


def modificarPersona(idPersona, nombre, apellidos, telefono,estatus):

    modificarPersona = db.session.query(Persona).filter(Persona.idPersona == idPersona).first()
    modificarPersona.nombre = nombre
    modificarPersona.apellidos = apellidos
    modificarPersona.telefono = telefono
    modificarPersona.estatus = estatus

    db.session.add(modificarPersona)
    db.session.flush()

    return modificarPersona.idPersona

def eliminarPersona(idPersona):
    eliminarPersonas = db.session.query(Persona).filter(Persona.idPersona == idPersona).first()
    db.session.delete(eliminarPersonas)
    db.session.commit()
    return True