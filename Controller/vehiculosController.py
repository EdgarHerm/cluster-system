from ..models import Vehiculo
from ..__init__ import dbSQL


def consultarVehiculo(idColono):
    if idColono == 0:
        return dbSQL.session.query(Vehiculo).all()
    else:
        return dbSQL.session.query(Vehiculo).filter(Vehiculo.idColono == idColono).first()

def agregarVehiculo(marca, modelo, color, matricula, fotografia,estatus, idColono):
    agregarVehiculos = Vehiculo(
        marcador=marca,
        modelo=modelo,
        color=color,
        matricula=matricula,
        fotografia=fotografia,
        estatus=estatus,
        idColono=idColono
    )

    dbSQL.session.add(agregarVehiculos)
    dbSQL.session.commit()
    return True

def modificarVehiculo(idVehiculo,marca,modelo,color,matricula,fotografia, estatus,idColono):
    modificarVehiculos = dbSQL.session.query(Vehiculo).filter(Vehiculo.idVehiculo == idVehiculo).first()
    modificarVehiculos.marcador=marca
    modificarVehiculos.modelo=modelo
    modificarVehiculos.color=color
    modificarVehiculos.matricula=matricula
    modificarVehiculos.fotografia=fotografia
    modificarVehiculos.estatus=estatus
    modificarVehiculos.idColono=idColono
    
    dbSQL.session.add(modificarVehiculos)
    dbSQL.session.commit()
    
    return True

def eliminarVehiculos(idVehiculo):
    eliminarVehiculos = dbSQL.session.query(Vehiculo).filter(Vehiculo.idVehiculo == idVehiculo).first()
    dbSQL.session.delete(eliminarVehiculos)
    dbSQL.session.commit()
    return True