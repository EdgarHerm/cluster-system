from ..models import Turno
from ..__init__ import db

def consultarTurno():
    return db.session.query(Turno)

def agregarTurno(horaInicio,horaFin):
    turno = Turno(
        horaInicio=horaInicio,
        horaFin=horaFin,
        estatus=1
    )
    db.session.add(turno)
    db.session.commit()
    return True

def modificarTurno(idTurno,horaInicio,horaFin):
    turno = db.session.query(Turno).filter(Turno.idTurno==idTurno).first()
    turno.horaInicio=horaInicio
    turno.horaFin=horaFin
    db.session.add(turno)
    db.session.commit()
    return True

def desactivarTurno(idTurno):
    turno = db.session.query(Turno).filter(Turno.idTurno==idTurno).first()
    turno.estatus=0
    db.session.add(turno)
    db.session.commit()
    return True

def activarTurno(idTurno):
    turno = db.session.query(Turno).filter(Turno.idTurno==idTurno).first()
    turno.estatus=1
    db.session.add(turno)
    db.session.commit()
    return True