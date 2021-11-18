from ..models import ListaPago
from ..__init__ import dbSQL

def consultarListaPago(idListaPago):
    if idListaPago == 0:
        return ListaPago.query.all()
    else:
        return dbSQL.session.query(ListaPago).filter(ListaPago.idListaPago == idListaPago).filter(ListaPago.estatus==1)
    
def agregarListaPago(motivoPago,monto,descripcion,fechaFin):

    agregarListaPago = ListaPago(
        motivoPago=motivoPago,
        monto=monto,
        descripcion=descripcion,
        fechaFin=fechaFin,
        estatus= 1
    )
    dbSQL.session.add(agregarListaPago)
    dbSQL.session.commit()
    return True

def modificarListaPago(idListaPago,motivoPago,monto,descripcion,fechaFin):
    modificarListaPago = dbSQL.session.query(ListaPago).filter(ListaPago.idListaPago == idListaPago).first()
    modificarListaPago.motivoPago= motivoPago
    modificarListaPago.monto=monto
    modificarListaPago.descripcion=descripcion
    modificarListaPago.fechaFin=fechaFin
    modificarListaPago.estatus=1
    dbSQL.session.add(modificarListaPago)
    dbSQL.session.commit()    
    return True

def desactivarListaPago(idListaPago):
    listaPago = dbSQL.session.query(ListaPago).filter(ListaPago.idListaPago == idListaPago).first()
    listaPago.estatus = 0
    dbSQL.session.add(listaPago)
    dbSQL.session.commit()
    
    return True

def activarListaPago(idListaPago):
    listaPago = dbSQL.session.query(ListaPago).filter(ListaPago.idListaPago == idListaPago).first()
    listaPago.estatus = 1
    dbSQL.session.add(listaPago)
    dbSQL.session.commit()
    
    return True