from ..models import Turno
from ..__init__ import dbSQL

def consultarTurno():
    return dbSQL.session.query(Turno).filter(Turno.estatus==1)

def agregarTurno(horaInicio,horaFin):
    turno = Turno(
        horaInicio=horaInicio,
        horaFin=horaFin,
        estatus=1
    )
    dbSQL.session.add(turno)
    dbSQL.session.commit()
    return True

def modificarTurno(idTurno,horaInicio,horaFin):
    turno = dbSQL.session.query(Turno).filter(Turno.idTurno==idTurno).first()
    turno.horaInicio=horaInicio
    turno.horaFin=horaFin
    dbSQL.session.add(turno)
    dbSQL.session.commit()
    return True

def desactivarTurno(idTurno):
    turno = dbSQL.session.query(Turno).filter(Turno.idTurno==idTurno).first()
    turno.estatus=0
    dbSQL.session.add(turno)
    dbSQL.session.commit()
    return True

def activarTurno(idTurno):
    turno = dbSQL.session.query(Turno).filter(Turno.idTurno==idTurno).first()
    turno.estatus=1
    dbSQL.session.add(turno)
    dbSQL.session.commit()
    return True