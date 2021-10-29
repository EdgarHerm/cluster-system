from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
import os
# Creamos una instancia de SQLAlchemy
dbSQL = SQLAlchemy()
from .models import Usuario, Rol

userDataStore = SQLAlchemyUserDatastore(dbSQL, Usuario, Rol)


def create_app():
    # Creamos una instancia del flask
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Generar la clave de sessión para crear una cookie con la inf. de la sessión
    app.config['SECRET_KEY'] = os.urandom(24)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://taurus:T4urus2021!@209.209.40.81:14818/cluster'

    app.config['SECURITY_PASSWORD_SALT'] = 'thissecretsalt'
    
    app.config['CORS_HEADERS'] = 'Content-Type'


    dbSQL.init_app(app)

    @app.before_first_request
    def create_all():
        dbSQL.create_all()

    from .Api.vehiculoApi import vehiculoApi as vehiculoApi
    app.register_blueprint(vehiculoApi)

    from .Api.colonoApi import colonoApi as colonoApi 
    app.register_blueprint(colonoApi)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    

    return app
