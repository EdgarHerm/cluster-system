from ..models import Usuario
from ..__init__ import db
import hashlib
import random


def consultarUsuario(idUsuario):
    if idUsuario == 0:
        return Usuario.query.all()
    else:
        return db.session.query(Usuario).filter(Usuario.idUsuario == idUsuario).first()
    
    
def insertarUsuario(correo, contraseña, idRol, estatus):
    agregarUsuario = Usuario(
        correo=correo,
        estatus=estatus,
        contraseña=contraseña, 
        token="", 
        idRol=idRol
    )

    db.session.add(agregarUsuario)
    db.session.flush()
    return agregarUsuario.idUsuario


def modificarUsuario(idUsuario, correo, contraseña, idRol , estatus):

    modificarUsuario = db.session.query(Usuario).filter(Usuario.idUsuario == idUsuario).first()
    modificarUsuario.correo = correo
    modificarUsuario.contraseña = contraseña
    modificarUsuario.token = ""
    modificarUsuario.idRol = idRol
    modificarUsuario.estatus = estatus

    db.session.add(modificarUsuario)
    db.session.flush()

    return modificarUsuario.idUsuario

def eliminarUsuario(idUsuario):
    eliminarUsuarios = db.session.query(Usuario).filter(Usuario.idUsuario == idUsuario).first()
    db.session.delete(eliminarUsuarios)
    db.session.commit()
    return True

def validarToken(token):
    if (db.session.query(Usuario).filter(Usuario.token == token).first()):
        return True
    else:
        return False
    
def login(usuario,contrasenia):
    result = db.session.query(Usuario).filter(Usuario.correo == usuario and Usuario.contraseña == contrasenia).first()
    
    if result is not None:
        h = hashlib.sha256(str(usuario+""+contrasenia).encode('utf-8')).hexdigest()
        
        result.token = h
        db.session.add(result)
        db.session.commit()
        
        return h

def logout(token):
    result = db.session.query(Usuario).filter(Usuario.token == token).first()
    if result: 
        result.token = "null"
        db.session.add(result) 
        db.session.commit()
        
        return True
    else:
        return False