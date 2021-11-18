from ..models import Vehiculo
from ..__init__ import db


def consultarVehiculo(idColono):
    if idColono == 0:
        return db.session.query(Vehiculo).all()
    else:
        return db.session.query(Vehiculo).filter(Vehiculo.idColono == idColono).first()

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

    db.session.add(agregarVehiculos)
    db.session.commit()
    return True

def modificarVehiculo(idVehiculo,marca,modelo,color,matricula,fotografia, estatus,idColono):
    modificarVehiculos = db.session.query(Vehiculo).filter(Vehiculo.idVehiculo == idVehiculo).first()
    modificarVehiculos.marcador=marca
    modificarVehiculos.modelo=modelo
    modificarVehiculos.color=color
    modificarVehiculos.matricula=matricula
    modificarVehiculos.fotografia=fotografia
    modificarVehiculos.estatus=estatus
    modificarVehiculos.idColono=idColono
    
    db.session.add(modificarVehiculos)
    db.session.commit()
    
    return True

def eliminarVehiculos(idVehiculo):
    eliminarVehiculos = db.session.query(Vehiculo).filter(Vehiculo.idVehiculo == idVehiculo).first()
    db.session.delete(eliminarVehiculos)
    db.session.commit()
    return True