import os
import click
from flask.cli import with_appcontext
from app.db import db

@click.command(name='create-db')
@with_appcontext
def create_database():
    root = os.path.dirname(os.path.abspath(__file__))
    db_dir = os.path.join(root, '../../database')
    if not os.path.exists(db_dir):
        os.mkdir(db_dir)
    db.create_all()

@click.command(name = 'create-upload')
@with_appcontext
def create_upload_folder():
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    uploaddir = os.path.join(root, '../../uploads')
    # make a directory if it doesn't exist
    if not os.path.exists(uploaddir):
        os.mkdir(uploaddir)

@click.command(name='create-log')
@with_appcontext
def create_log_folder():
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, '../../logs')
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)