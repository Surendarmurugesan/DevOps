## This file used for automatically package has download while we initate the "Import"

from flask import Flask, app

def create_app():
    app = Flask(__name__)    # Name of the file
    app.config['SECRET_KEY'] = 'dsfijdfkdsfkj'  ## Variable configure here, its some confidential value so func has encrypt the value related to our website.
    return app