from ..models import Domicilio
from ..__init__ import db

def consultarDomicilio(idDomicilio):
    if idDomicilio == 0:
        return db.session.query(Domicilio).filter(Domicilio.estatus == 1).all()
    else:
        return db.session.query(Domicilio).filter(Domicilio.idDomicilio == idDomicilio).filter(Domicilio.estatus == 1).first()

def agregarDomicilio(calle,numero,descripcion):
    agregarDomicilios = Domicilio(
        calle=calle,
        numero=numero,
        descripcion=descripcion,
        estatus=1
    )

    db.session.add(agregarDomicilios)
    db.session.commit()
    return True

def modificarDomicilio(idDomicilio,calle,numero,descripcion,):
    modificarDomicilios = db.session.query(Domicilio).filter(Domicilio.idDomicilio == idDomicilio).first()
    modificarDomicilios.calle=calle
    modificarDomicilios.numero=numero
    modificarDomicilios.descripcion=descripcion
    modificarDomicilios.estatus=1
    
    db.session.add(modificarDomicilios)
    db.session.commit()
    
    return True

def eliminarDomicilios(idDomicilio):
    eliminarDomicilios = db.session.query(Domicilio).filter(Domicilio.idDomicilio == idDomicilio).first()
    db.session.delete(eliminarDomicilios)
    db.session.commit()
    return True
def desactivarDomicilio(idDomicilio):
    
    domicilio = db.session.query(Domicilio).filter(
        Domicilio.idDomicilio == idDomicilio).first()
    domicilio.estatus=0
    db.session.add(domicilio)
    db.session.commit()
    
    return True

def activarDomicilio(idDomicilio):

    domicilio = db.session.query(Domicilio).filter(
        Domicilio.idDomicilio == idDomicilio).first()
    domicilio.estatus=1
    db.session.add(domicilio)
    db.session.commit()
    
    return True