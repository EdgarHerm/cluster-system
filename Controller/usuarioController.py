from ..models import Usuario
from ..__init__ import dbSQL
import hashlib
from datetime import datetime


def consultarUsuario(idUsuario):
    if idUsuario == 0:
        return Usuario.query.all()
    else:
        return dbSQL.session.query(Usuario).filter(Usuario.idUsuario == idUsuario).first()
    
    
def insertarUsuario(correo, contraseña, idRol, estatus):
    agregarUsuario = Usuario(
        correo=correo,
        estatus=estatus,
        contraseña=contraseña,  
        idRol=idRol
    )

    dbSQL.session.add(agregarUsuario)
    dbSQL.session.flush()
    return agregarUsuario.idUsuario


def modificarUsuario(idUsuario, correo, contraseña, idRol , estatus):

    modificarUsuario = dbSQL.session.query(Usuario).filter(Usuario.idUsuario == idUsuario).first()
    modificarUsuario.correo = correo
    modificarUsuario.contraseña = contraseña
    modificarUsuario.idRol = idRol
    modificarUsuario.estatus = estatus

    dbSQL.session.add(modificarUsuario)
    dbSQL.session.flush()

    return modificarUsuario.idUsuario

def eliminarUsuario(idUsuario):
    eliminarUsuarios = dbSQL.session.query(Usuario).filter(Usuario.idUsuario == idUsuario).first()
    dbSQL.session.delete(eliminarUsuarios)
    dbSQL.session.commit()
    return True

def validarToken(token):
    if (dbSQL.session.query(Usuario).filter(Usuario.token == token).first()):
        return True
    else:
        return False
    
def login(usuario,contrasenia):
    fecha = datetime.today()
    result = dbSQL.session.query(Usuario).filter(Usuario.correo == usuario and Usuario.contraseña == contrasenia).first()
    
    if result is not None:
        h = hashlib.new("hash", usuario+"-"+contrasenia+"-"+fecha)
        
        result.token = h.hexdigest()
        dbSQL.session.add(result)
        dbSQL.session.commit()
        
        return h.hexdigest()

def logout(token):
    result = dbSQL.session.query(Usuario).filter(Usuario.token == token).first()
    if result: 
        result.token = "null"
        dbSQL.session.add(result) 
        dbSQL.session.commit()
        
        return True
    else:
        return False