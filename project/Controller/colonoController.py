from ..models import Colono, Persona, Usuario, Domicilio
from .domicilioController import *
from .personaController import *
from .usuarioController import *
from ..__init__ import db


def consultarColono(idColono):
    if idColono == 0:
        return db.session.query(Colono, Persona, Usuario, Domicilio).join(Persona, Persona.idPersona == Colono.idPersona).join(Usuario, Usuario.idUsuario == Colono.idUsuario).join(Domicilio, Domicilio.idDomicilio == Colono.idDomicilio).filter(Colono.estatus==1)

    else:
        return db.session.query(Colono, Persona, Usuario, Domicilio).join(Persona, Persona.idPersona == Colono.idPersona).join(Usuario, Usuario.idUsuario == Colono.idUsuario).join(Domicilio, Domicilio.idDomicilio == Colono.idDomicilio).filter(Colono.idColono == idColono).filter(Colono.estatus==1)


def agregarColono(foto,correo, contraseña, idRol, nombre, apellidos, telefono, idDomicilio) :
    estatus =1

    persona = insertarPersona(nombre, apellidos, telefono)

    usuario = insertarUsuario(correo, contraseña, idRol, estatus)

    

    colono = Colono(
        fotografia=foto,
        estatus=estatus,
        idDomicilio=idDomicilio,
        idPersona=persona,
        idUsuario=usuario,

    )
    db.session.add(colono)
    db.session.commit()
    return True


def modificarColono(idColono, idUsuario, idPersona, idDomicilio, foto, correo, contraseña, idRol, nombre, apellidos, telefono):
    estatus=1

    persona = modificarPersona(idPersona, nombre, apellidos, telefono,estatus)

    usuario = modificarUsuario(idUsuario, correo, contraseña, idRol,estatus)


    colono = db.session.query(Colono).filter(
        Colono.idColono == idColono).first()
    colono.fotografia = foto
    colono.estatus=estatus
    colono.idDomicilio=idDomicilio
    colono.idPersona=persona
    colono.idUsuario=usuario
    db.session.add(colono)
    db.session.commit()

    return True


def desactivarColono(idColono):
    
    colono = db.session.query(Colono).filter(
        Colono.idColono == idColono).first()
    colono.estatus=0
    db.session.add(colono)
    db.session.commit()
    
    return True

def activarColono(idColono):

    colono = db.session.query(Colono).filter(
        Colono.idColono == idColono).first()
    colono.estatus=1
    db.session.add(colono)
    db.session.commit()
    
    return True