from . import dbSQL
from datetime import datetime

hoy = datetime.now()
# Definiendo la tabla relacional

class ListaPago(dbSQL.Model):
    """ListaPago Model"""

    __tablename__ = 'ListaPago'
    idListaPago = dbSQL.Column(dbSQL.Integer, primary_key=True)
    motivoPago = dbSQL.Column(dbSQL.String(80),nullable=False)
    monto = dbSQL.Column(dbSQL.Float,nullable=False)
    descripcion = dbSQL.Column(dbSQL.String(80),nullable=False)
    fechaInicio = dbSQL.Column(dbSQL.DateTime, default = hoy)
    fechaFin = dbSQL.Column(dbSQL.DateTime,default = False)
    estatus = dbSQL.Column(dbSQL.Integer, nullable=False)

class Rol(dbSQL.Model):
    """Rol Model"""
    
    __tablename__ = 'Rol'
    idRol = dbSQL.Column(dbSQL.Integer, primary_key=True)
    nombre = dbSQL.Column(dbSQL.String(50), nullable=False)
    descripcion = dbSQL.Column(dbSQL.String(255))
    
class Usuario(dbSQL.Model):
    """Usuario Model"""
    
    __tablename__ = 'Usuario'
    idUsuario = dbSQL.Column(dbSQL.Integer, primary_key=True)
    correo = dbSQL.Column(dbSQL.String(64) , nullable=False)
    estatus = dbSQL.Column(dbSQL.Integer, nullable=False)
    contraseña = dbSQL.Column(dbSQL.String(64) , nullable=False)
    token = dbSQL.Column(dbSQL.Text() , nullable=False)
    idRol= dbSQL.Column('idRol', dbSQL.Integer,dbSQL.ForeignKey('Rol.idRol'))
    rol = dbSQL.relationship('Rol', backref=dbSQL.backref('roles', lazy='dynamic'))
    
class Turno(dbSQL.Model):
    """Turno Model"""
    
    __tablename__ = 'Turno'
    idTurno = dbSQL.Column(dbSQL.Integer, primary_key=True)
    horaInicio = dbSQL.Column(dbSQL.String(20) , nullable=False)
    horaFin = dbSQL.Column(dbSQL.String(20) , nullable=False)
    estatus = dbSQL.Column(dbSQL.Integer, nullable=False)
    
class Persona(dbSQL.Model):
    """ Persona model"""

    __tablename__="Persona"
    idPersona = dbSQL.Column(dbSQL.Integer, primary_key=True)
    nombre= dbSQL.Column(dbSQL.String(50), nullable=False)
    apellidos= dbSQL.Column(dbSQL.String(50), nullable=False)
    telefono= dbSQL.Column(dbSQL.String(12), nullable=False)
    
class Empleado(dbSQL.Model):
    """Empleado Model"""
    
    __tablename__ = 'Empleado'
    idEmpleado = dbSQL.Column(dbSQL.Integer, primary_key=True)
    empresador = dbSQL.Column(dbSQL.String(30), nullable=False)
    zona = dbSQL.Column(dbSQL.String(20), nullable=False)
    estatus = dbSQL.Column(dbSQL.Integer, nullable=False)
    idTurno= dbSQL.Column('idTurno', dbSQL.Integer,dbSQL.ForeignKey('Turno.idTurno'))
    rol = dbSQL.relationship('Turno', backref=dbSQL.backref('turnos', lazy='dynamic'))
    idPersona= dbSQL.Column('idPersona', dbSQL.Integer,dbSQL.ForeignKey('Persona.idPersona'))
    persona = dbSQL.relationship('Persona', backref=dbSQL.backref('personasEmpleado', lazy='dynamic'))
    idUsuario= dbSQL.Column('idUsuario', dbSQL.Integer,dbSQL.ForeignKey('Usuario.idUsuario'))
    usuario = dbSQL.relationship('Usuario', backref=dbSQL.backref('usuariosEmpleado', lazy='dynamic'))
    
class Domicilio(dbSQL.Model):
    """Domicilio Model"""
    
    __tablename__ = 'Domicilio'
    idDomicilio = dbSQL.Column(dbSQL.Integer,primary_key=True)
    calle = dbSQL.Column(dbSQL.String(45), nullable=False)
    numero = dbSQL.Column(dbSQL.String(10), nullable=False)
    descripcion = dbSQL.Column(dbSQL.String(50), nullable=False)
    estatus = dbSQL.Column(dbSQL.Integer, nullable=False)
    

class Colono(dbSQL.Model):
    """Colono Model"""
    
    __tablename__ = 'Colono'
    idColono= dbSQL.Column(dbSQL.Integer, primary_key=True)
    fotografia = dbSQL.Column(dbSQL.Text(), nullable=False)
    estatus = dbSQL.Column(dbSQL.Integer, nullable=False)
    idDomicilio= dbSQL.Column('idDomicilio', dbSQL.Integer,dbSQL.ForeignKey('Domicilio.idDomicilio'))
    domicilio = dbSQL.relationship('Domicilio', backref=dbSQL.backref('domicilio', lazy='dynamic'))
    idPersona= dbSQL.Column('idPersona', dbSQL.Integer,dbSQL.ForeignKey('Persona.idPersona'))
    persona = dbSQL.relationship('Persona', backref=dbSQL.backref('personasColono', lazy='dynamic'))
    idUsuario= dbSQL.Column('idUsuario', dbSQL.Integer,dbSQL.ForeignKey('Usuario.idUsuario'))
    usuario = dbSQL.relationship('Usuario', backref=dbSQL.backref('usuariosColono', lazy='dynamic'))
    
class Vehiculo(dbSQL.Model):
    """Vehiculo Model"""
    
    __tablename__ = 'Vehiculo'
    idVehiculo = dbSQL.Column(dbSQL.Integer,primary_key=True)
    marcador = dbSQL.Column(dbSQL.String(30), nullable=False)
    modelo = dbSQL.Column(dbSQL.String(30), nullable=False)
    color = dbSQL.Column(dbSQL.String(20), nullable=False)
    matricula = dbSQL.Column(dbSQL.String(20), nullable=False)
    fotografia = dbSQL.Column(dbSQL.Text(), nullable=False)
    estatus = dbSQL.Column(dbSQL.Integer, nullable=False)
    idColono= dbSQL.Column('idColono', dbSQL.Integer,dbSQL.ForeignKey('Colono.idColono'))
    colono = dbSQL.relationship('Colono', backref=dbSQL.backref('colonosVehiculo', lazy='dynamic'))
    
class Visita(dbSQL.Model):
    """Visita Model"""
    
    __tablename__ = 'Visita'
    idVisita= dbSQL.Column(dbSQL.Integer, primary_key=True)
    nombre = dbSQL.Column(dbSQL.String(50), nullable=False)
    matriculaVehiculo = dbSQL.Column(dbSQL.String(20), nullable=False)
    modelo = dbSQL.Column(dbSQL.String(30), nullable=False)
    color= dbSQL.Column(dbSQL.String(20), nullable=False)
    estatus = dbSQL.Column(dbSQL.Integer, nullable=False)
    fechaEntrada= dbSQL.Column(dbSQL.DateTime,default = hoy)
    fechaSalida= dbSQL.Column(dbSQL.DateTime,nullable=False)
    idColono= dbSQL.Column('idColono', dbSQL.Integer,dbSQL.ForeignKey('Colono.idColono'))
    colono = dbSQL.relationship('Colono', backref=dbSQL.backref('colonosVisita', lazy='dynamic'))
    
class RecepcionPago(dbSQL.Model):
    """RecepcionPago Model"""
    
    __tablename__ = 'RecepcionPago'
    idRecepcionPago= dbSQL.Column(dbSQL.Integer, primary_key=True)
    fechaPago = dbSQL.Column(dbSQL.DateTime,nullable=False)
    fotEvidencia = dbSQL.Column(dbSQL.Text(), nullable=False)
    fechaRecepcion= dbSQL.Column(dbSQL.DateTime,nullable=False)
    descripcion = dbSQL.Column(dbSQL.String(50), nullable=False)
    estatus = dbSQL.Column(dbSQL.Integer, nullable=False)
    idColono= dbSQL.Column('idColono', dbSQL.Integer,dbSQL.ForeignKey('Colono.idColono'))
    colono = dbSQL.relationship('Colono', backref=dbSQL.backref('colonosPagos', lazy='dynamic'))
    idListaPago= dbSQL.Column('idListaPago', dbSQL.Integer,dbSQL.ForeignKey('ListaPago.idListaPago'))
    listapago = dbSQL.relationship('ListaPago', backref=dbSQL.backref('listapagos', lazy='dynamic'))



