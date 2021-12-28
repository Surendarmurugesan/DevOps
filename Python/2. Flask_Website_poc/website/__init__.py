## This file used for automatically package has download while we initate the "Import"

from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)    # Name of the file
    app.config['SECRET_KEY'] = 'dsfijdfkdsfkj'  ## Variable configure here, its some confidential value so func has encrypt the value related to our website.
    app.config['SQLAlCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') ## if we given any prefix path ex:'/auth-path/' output:localhost:5000/auth-path/login

    return app