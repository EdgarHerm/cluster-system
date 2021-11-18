from . import db
from datetime import datetime

hoy = datetime.now()
# Definiendo la tabla relacional

class ListaPago(db.Model):
    """ListaPago Model"""

    __tablename__ = 'ListaPago'
    idListaPago = db.Column(db.Integer, primary_key=True)
    motivoPago = db.Column(db.String(80),nullable=False)
    monto = db.Column(db.Float,nullable=False)
    descripcion = db.Column(db.String(80),nullable=False)
    fechaInicio = db.Column(db.DateTime, default = hoy)
    fechaFin = db.Column(db.DateTime,default = False)
    estatus = db.Column(db.Integer, nullable=False)

class Rol(db.Model):
    """Rol Model"""
    
    __tablename__ = 'Rol'
    idRol = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(255))
    
class Usuario(db.Model):
    """Usuario Model"""
    
    __tablename__ = 'Usuario'
    idUsuario = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(64) , nullable=False)
    estatus = db.Column(db.Integer, nullable=False)
    contraseña = db.Column(db.String(64) , nullable=False)
    token = db.Column(db.Text() , nullable=False)
    idRol= db.Column('idRol', db.Integer,db.ForeignKey('Rol.idRol'))
    rol = db.relationship('Rol', backref=db.backref('roles', lazy='dynamic'))
    
class Turno(db.Model):
    """Turno Model"""
    
    __tablename__ = 'Turno'
    idTurno = db.Column(db.Integer, primary_key=True)
    horaInicio = db.Column(db.String(20) , nullable=False)
    horaFin = db.Column(db.String(20) , nullable=False)
    estatus = db.Column(db.Integer, nullable=False)
    
class Persona(db.Model):
    """ Persona model"""

    __tablename__="Persona"
    idPersona = db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(50), nullable=False)
    apellidos= db.Column(db.String(50), nullable=False)
    telefono= db.Column(db.String(12), nullable=False)
    
class Empleado(db.Model):
    """Empleado Model"""
    
    __tablename__ = 'Empleado'
    idEmpleado = db.Column(db.Integer, primary_key=True)
    empresador = db.Column(db.String(30), nullable=False)
    zona = db.Column(db.String(20), nullable=False)
    estatus = db.Column(db.Integer, nullable=False)
    idTurno= db.Column('idTurno', db.Integer,db.ForeignKey('Turno.idTurno'))
    rol = db.relationship('Turno', backref=db.backref('turnos', lazy='dynamic'))
    idPersona= db.Column('idPersona', db.Integer,db.ForeignKey('Persona.idPersona'))
    persona = db.relationship('Persona', backref=db.backref('personasEmpleado', lazy='dynamic'))
    idUsuario= db.Column('idUsuario', db.Integer,db.ForeignKey('Usuario.idUsuario'))
    usuario = db.relationship('Usuario', backref=db.backref('usuariosEmpleado', lazy='dynamic'))
    
class Domicilio(db.Model):
    """Domicilio Model"""
    
    __tablename__ = 'Domicilio'
    idDomicilio = db.Column(db.Integer,primary_key=True)
    calle = db.Column(db.String(45), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    descripcion = db.Column(db.String(50), nullable=False)
    estatus = db.Column(db.Integer, nullable=False)
    

class Colono(db.Model):
    """Colono Model"""
    
    __tablename__ = 'Colono'
    idColono= db.Column(db.Integer, primary_key=True)
    fotografia = db.Column(db.Text(), nullable=False)
    estatus = db.Column(db.Integer, nullable=False)
    idDomicilio= db.Column('idDomicilio', db.Integer,db.ForeignKey('Domicilio.idDomicilio'))
    domicilio = db.relationship('Domicilio', backref=db.backref('domicilio', lazy='dynamic'))
    idPersona= db.Column('idPersona', db.Integer,db.ForeignKey('Persona.idPersona'))
    persona = db.relationship('Persona', backref=db.backref('personasColono', lazy='dynamic'))
    idUsuario= db.Column('idUsuario', db.Integer,db.ForeignKey('Usuario.idUsuario'))
    usuario = db.relationship('Usuario', backref=db.backref('usuariosColono', lazy='dynamic'))
    
class Vehiculo(db.Model):
    """Vehiculo Model"""
    
    __tablename__ = 'Vehiculo'
    idVehiculo = db.Column(db.Integer,primary_key=True)
    marcador = db.Column(db.String(30), nullable=False)
    modelo = db.Column(db.String(30), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    matricula = db.Column(db.String(20), nullable=False)
    fotografia = db.Column(db.Text(), nullable=False)
    estatus = db.Column(db.Integer, nullable=False)
    idColono= db.Column('idColono', db.Integer,db.ForeignKey('Colono.idColono'))
    colono = db.relationship('Colono', backref=db.backref('colonosVehiculo', lazy='dynamic'))
    
class Visita(db.Model):
    """Visita Model"""
    
    __tablename__ = 'Visita'
    idVisita= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    matriculaVehiculo = db.Column(db.String(20), nullable=False)
    modelo = db.Column(db.String(30), nullable=False)
    color= db.Column(db.String(20), nullable=False)
    estatus = db.Column(db.Integer, nullable=False)
    fechaEntrada= db.Column(db.DateTime,default = hoy)
    fechaSalida= db.Column(db.DateTime,nullable=False)
    idColono= db.Column('idColono', db.Integer,db.ForeignKey('Colono.idColono'))
    colono = db.relationship('Colono', backref=db.backref('colonosVisita', lazy='dynamic'))
    
class RecepcionPago(db.Model):
    """RecepcionPago Model"""
    
    __tablename__ = 'RecepcionPago'
    idRecepcionPago= db.Column(db.Integer, primary_key=True)
    fechaPago = db.Column(db.DateTime,nullable=False)
    fotEvidencia = db.Column(db.Text(), nullable=False)
    fechaRecepcion= db.Column(db.DateTime,nullable=False)
    descripcion = db.Column(db.String(50), nullable=False)
    estatus = db.Column(db.Integer, nullable=False)
    idColono= db.Column('idColono', db.Integer,db.ForeignKey('Colono.idColono'))
    colono = db.relationship('Colono', backref=db.backref('colonosPagos', lazy='dynamic'))
    idListaPago= db.Column('idListaPago', db.Integer,db.ForeignKey('ListaPago.idListaPago'))
    listapago = db.relationship('ListaPago', backref=db.backref('listapagos', lazy='dynamic'))



