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
from app.cli import create_database,create_upload_folder,create_log_folder
from app.db import db
from app.db.models import User, Transaction
from app.pnf_error import pnf_error
from app.simple_pages import simple_pages
from app.auth import auth
from app.context_processors import utility_text_processors
from app.transactions import transactions

login_manager = flask_login.LoginManager()

@login_manager.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = 'This is an INSECURE secret!! DO NOT use this in production!!'

    #app.register_error_handler(404, page_not_found)
    db_dir = "database/db.sqlite"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.abspath(db_dir)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #Should the very first commands being executed
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    csrf = CSRFProtect(app)
    bootstrap = Bootstrap5(app)

    #Needed for Forms
    app.context_processor(utility_text_processors)

    #Our Pages with interfaces
    app.register_blueprint(simple_pages)
    app.register_blueprint(auth)
    #Pages with Functionality but no interfaces
    app.register_blueprint(pnf_error)
    app.register_blueprint(transactions)
    # add command function to cli commands
    app.cli.add_command(create_database)
    app.cli.add_command(create_upload_folder)
    app.cli.add_command(create_log_folder)
    db.init_app(app)
    #def hello():
    #    return 'Hello, World!'

    return app