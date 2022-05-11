"""Bank Transaction - This will hold the base of the app"""
#OS and Logging
import os
import logging
from logging.handlers import RotatingFileHandler

#Flask
import flask_login
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

#App
from app.cli import create_database
from app.db import db
from app.db.models import User
from app.pnf_error import page_not_found


login_manager = flask_login.LoginManager()

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = 'This is an INSECURE secret!! DO NOT use this in production!!'

    #app.register_error_handler(404, page_not_found)
    db_dir = "database/db.sqlite"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.abspath(db_dir)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # add command function to cli commands
    app.cli.add_command(create_database)

    #These should


    db.init_app(app)
    #def hello():
    #    return 'Hello, World!'

    return app