from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
import os
# Creamos una instancia de SQLAlchemy

dbSQL = SQLAlchemy()
from . models import Usuario,Rol
userDataStore = SQLAlchemyUserDatastore(dbSQL, Usuario, Rol)

def create_app():
    # Creamos una instancia del flask
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Generar la clave de sessión para crear una cookie con la inf. de la sessión
    app.config['SECRET_KEY'] = os.urandom(24)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root12@localhost:3303/cluster'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pizzadev:idgs801!@192.168.0.108:3306/tiendaflask'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pizzadev:idgs801!@192.168.0.108:3306/tiendaflask'

    app.config['SECURITY_PASSWORD_SALT'] = 'thissecretsalt'
    dbSQL.init_app(app)

    @app.before_first_request
    def create_all():
        dbSQL.create_all()
        
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app