from ..models import Visita, Colono, Domicilio,Persona
from ..__init__ import db
from datetime import datetime


def consultarVisitas(idVisita):
    if idVisita == 0:
        return db.session.query(Visita, Colono, Domicilio).join(Colono, Colono.idColono == Visita.idColono).join(Domicilio, Domicilio.idDomicilio == Colono.idDomicilio).join(Persona, Persona.idPersona== Colono.idPersona).all()
    else:
        return db.session.query(Visita, Colono, Domicilio).join(Colono, Colono.idColono == Visita.idColono).join(Domicilio, Domicilio.idDomicilio == Colono.idDomicilio).join(Persona, Persona.idPersona== Colono.idPersona).filter(Visita.idVisita == idVisita).first()


def consultarVisitasEmpleado(idColono):
    if idColono == 0:
        return db.session.query(Visita, Colono, Domicilio,Persona).join(Colono, Colono.idColono == Visita.idColono).join(Domicilio, Domicilio.idDomicilio == Colono.idDomicilio).join(Persona, Persona.idPersona== Colono.idPersona).all()
    else:
        return db.session.query(Visita, Colono, Domicilio).join(Colono, Colono.idColono == Visita.idColono).join(Domicilio, Domicilio.idDomicilio == Colono.idDomicilio).join(Persona, Persona.idPersona== Colono.idPersona).filter(Visita.idColono == idColono).all()

def agregarVisitas(nombre, matricula, modelo, color, idColono):

    visita = Visita(
        nombre=nombre,
        matriculaVehiculo=matricula,
        modelo=modelo,
        color=color,
        estatus=1,
        fechaEntrada="2000-01-01 00:00:00",
        fechaSalida="2000-01-01 00:00:00",
        idColono=idColono
    )

    db.session.add(visita)
    db.session.commit()

    return True


def modificarVisita(idVisita, nombre, matricula, modelo, color):
    visita = db.session.query(Visita).filter(
        Visita.idVisita == idVisita).first()
    visita.nombre = nombre
    visita.matriculaVehiculo = matricula
    visita.modelo = modelo
    visita.color = color

    db.session.add(visita)
    db.session.commit()
    return True


def entradaVisita(idVisita):
    entrada = datetime.now()
    visita = db.session.query(Visita).filter(
        Visita.idVisita == idVisita).first()
    visita.fechaEntrada = entrada

    db.session.add(visita)
    db.session.commit()

    return True


def salidaVisita(idVisita):
    salida = datetime.now()
    visita = db.session.query(Visita).filter(
        Visita.idVisita == idVisita).first()
    visita.fechaSalida = salida

    db.session.add(visita)
    db.session.commit()

    return True


def cancelarVisita(idVisita):
    visita = db.session.query(Visita).filter(
        Visita.idVisita == idVisita).first()
    visita.estatus = 0

    db.session.add(visita)
    db.session.commit()

    return True
