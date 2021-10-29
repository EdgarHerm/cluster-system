from ..models import Domicilio
from ..__init__ import dbSQL

def consultarDomicilio(idDomicilio):
    if idDomicilio == 0:
        return Domicilio.query.all()
    else:
        return dbSQL.session.query(Domicilio).filter(Domicilio.idDomicilio == idDomicilio).first()

def agregarDomicilio(calle,numero,descripcion,estatus):
    agregarDomicilios = Domicilio(
        calle=calle,
        numero=numero,
        descripcion=descripcion,
        estatus=estatus
    )

    dbSQL.session.add(agregarDomicilios)
    dbSQL.session.flush()
    return agregarDomicilios.idDomicilio

def modificarDomicilio(idDomicilio,calle,numero,descripcion,estatus):
    modificarDomicilios = dbSQL.session.query(Domicilio).filter(Domicilio.idDomicilio == idDomicilio).first()
    modificarDomicilios.calle=calle
    modificarDomicilios.numero=numero
    modificarDomicilios.descripcion=descripcion
    modificarDomicilios.estatus=estatus
    
    dbSQL.session.add(modificarDomicilios)
    dbSQL.session.flush()
    
    return modificarDomicilios.idDomicilio

def eliminarDomicilios(idDomicilio):
    eliminarDomicilios = dbSQL.session.query(Domicilio).filter(Domicilio.idDomicilio == idDomicilio).first()
    dbSQL.session.delete(eliminarDomicilios)
    dbSQL.session.commit()
    return True