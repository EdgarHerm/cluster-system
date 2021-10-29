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
    return True