from models import Vehiculo
from . import dbSQL




def consultarVehiculo():
    return Vehiculo.query.all()