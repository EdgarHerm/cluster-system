from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
import os


# Creamos una instancia de SQLAlchemy
db = SQLAlchemy()

from .models import Usuario, Rol

userDataStore = SQLAlchemyUserDatastore(db, Usuario, Rol)


def create_app():
    # Creamos una instancia del flask
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Generar la clave de sessión para crear una cookie con la inf. de la sessión
    app.config['SECRET_KEY'] = os.urandom(24)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://taurus:T4urus2021_!@172.107.32.118:19966/cluster'

    app.config['SECURITY_PASSWORD_SALT'] = 'thissecretsalt'
    
    app.config['CORS_HEADERS'] = 'Content-Type'


    db.init_app(app)

    @app.before_first_request
    def create_all():
        db.create_all()

    from .Api.vehiculoApi import vehiculoApi as vehiculoApi
    app.register_blueprint(vehiculoApi)

    from .Api.listaPagoApi import listaPagoApi as listaPagoApi
    app.register_blueprint(listaPagoApi)

    from .Api.empleadoApi import empleadoApi as empleadoApi
    app.register_blueprint(empleadoApi)

    from .Api.colonoApi import colonoApi as colonoApi 
    app.register_blueprint(colonoApi)

    from .Api.turnosApi import turnoApi as turnosApi  
    app.register_blueprint(turnosApi)
    
    from .Api.domicilioApi import domicilioApi as domicilioApi  
    app.register_blueprint(domicilioApi)
    
    from .Api.loginApi import sesionApi as sesionApi  
    app.register_blueprint(sesionApi)
    
    # from .main import main as mains
    # app.register_blueprint(mains)
    
    

    return app
