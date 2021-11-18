from ..models import ListaPago
from ..__init__ import db

def consultarListaPago(idListaPago):
    if idListaPago == 0:
        return ListaPago.query.all()
    else:
        return db.session.query(ListaPago).filter(ListaPago.idListaPago == idListaPago).filter(ListaPago.estatus==1)
    
def agregarListaPago(motivoPago,monto,descripcion,fechaFin):

    agregarListaPago = ListaPago(
        motivoPago=motivoPago,
        monto=monto,
        descripcion=descripcion,
        fechaFin=fechaFin,
        estatus= 1
    )
    db.session.add(agregarListaPago)
    db.session.commit()
    return True

def modificarListaPago(idListaPago,motivoPago,monto,descripcion,fechaFin):
    modificarListaPago = db.session.query(ListaPago).filter(ListaPago.idListaPago == idListaPago).first()
    modificarListaPago.motivoPago= motivoPago
    modificarListaPago.monto=monto
    modificarListaPago.descripcion=descripcion
    modificarListaPago.fechaFin=fechaFin
    modificarListaPago.estatus=1
    db.session.add(modificarListaPago)
    db.session.commit()    
    return True

def desactivarListaPago(idListaPago):
    listaPago = db.session.query(ListaPago).filter(ListaPago.idListaPago == idListaPago).first()
    listaPago.estatus = 0
    db.session.add(listaPago)
    db.session.commit()
    
    return True

def activarListaPago(idListaPago):
    listaPago = db.session.query(ListaPago).filter(ListaPago.idListaPago == idListaPago).first()
    listaPago.estatus = 1
    db.session.add(listaPago)
    db.session.commit()
    
    return True