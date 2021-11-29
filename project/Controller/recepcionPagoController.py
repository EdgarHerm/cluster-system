from ..models import RecepcionPago, Colono, ListaPago,Persona
from ..__init__ import db

def consultarRecepcion(idRecepcionPago):
    if idRecepcionPago == 0:
        return db.session.query(RecepcionPago,ListaPago,Colono,Persona).join(Colono, Colono.idColono == RecepcionPago.idColono).join(ListaPago, ListaPago.idListaPago == RecepcionPago.idListaPago).join(Persona, Persona.idPersona == Colono.idPersona).all()
    else:
        return db.session.query(RecepcionPago,ListaPago,Colono,Persona).join(Colono, Colono.idColono == RecepcionPago.idColono).join(ListaPago, ListaPago.idListaPago == RecepcionPago.idListaPago).join(Persona, Persona.idPersona == Colono.idPersona).filter(RecepcionPago.idRecepcionPago == idRecepcionPago).first()
    
def agregarRecepcion(fechaPago,fotEvidencia,fechaRecepcion,descripcion,idColono,idListaPago):
    Recepcion = RecepcionPago(
        fechaPago=fechaPago,
        fotEvidencia=fotEvidencia,
        fechaRecepcion=fechaRecepcion,
        descripcion=descripcion,
        estatus = 2,
        idColono=idColono,
        idListaPago=idListaPago
    )
    db.session.add(Recepcion)
    db.session.commit()
    return True

def modificarRecepcion (idRecepcionPago,fechaPago,fotEvidencia,descripcion,):
    Recepcion = db.session.query(RecepcionPago).filter(RecepcionPago.idRecepcionPago == idRecepcionPago).first()
    Recepcion.fechaPago = fechaPago
    Recepcion.fotEvidencia = fotEvidencia
    Recepcion.descripcion = descripcion
    db.session.add(Recepcion)
    db.session.commit()
    return True

def cancelarRecepcion(idRecepcionPago):
    Recepcion = db.session.query(RecepcionPago).filter(RecepcionPago.idRecepcionPago == idRecepcionPago).first()
    Recepcion.estatus =0
    db.session.add(Recepcion)
    db.session.commit()
    return True


def aceptarRecepcion(idRecepcionPago):
    Recepcion = db.session.query(RecepcionPago).filter(RecepcionPago.idRecepcionPago == idRecepcionPago).first()
    Recepcion.estatus =1
    db.session.add(Recepcion)
    db.session.commit()
    return True