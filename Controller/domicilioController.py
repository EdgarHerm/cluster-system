from ..models import Domicilio
from ..__init__ import dbSQL

def consultarDomicilio(idDomicilio):
    if idDomicilio == 0:
        return Domicilio.query.all()
    else:
        return dbSQL.session.query(Domicilio).filter(Domicilio.idDomicilio == idDomicilio).first()

def agregarDomicilio(calle,numero,descripcion):
    agregarDomicilios = Domicilio(
        calle=calle,
        numero=numero,
        descripcion=descripcion,
        estatus=1
    )

    dbSQL.session.add(agregarDomicilios)
    dbSQL.session.commit()
    return True

def modificarDomicilio(idDomicilio,calle,numero,descripcion,):
    modificarDomicilios = dbSQL.session.query(Domicilio).filter(Domicilio.idDomicilio == idDomicilio).first()
    modificarDomicilios.calle=calle
    modificarDomicilios.numero=numero
    modificarDomicilios.descripcion=descripcion
    modificarDomicilios.estatus=1
    
    dbSQL.session.add(modificarDomicilios)
    dbSQL.session.commit()
    
    return True

def eliminarDomicilios(idDomicilio):
    eliminarDomicilios = dbSQL.session.query(Domicilio).filter(Domicilio.idDomicilio == idDomicilio).first()
    dbSQL.session.delete(eliminarDomicilios)
    dbSQL.session.commit()
    return True
def desactivarDomicilio(idDomicilio):
    
    domicilio = dbSQL.session.query(Domicilio).filter(
        Domicilio.idDomicilio == idDomicilio).first()
    domicilio.estatus=0
    dbSQL.session.add(domicilio)
    dbSQL.session.commit()
    
    return True

def activarDomicilio(idDomicilio):

    domicilio = dbSQL.session.query(Domicilio).filter(
        Domicilio.idDomicilio == idDomicilio).first()
    domicilio.estatus=1
    dbSQL.session.add(domicilio)
    dbSQL.session.commit()
    
    return True