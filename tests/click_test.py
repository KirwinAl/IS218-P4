'''Testing for files and directories'''
import os
from click.testing import CliRunner
from app import create_log_folder, create_database, create_upload_folder
runner = CliRunner()


def test_create_log_folder():
    '''Searches if the logs folder exists'''
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, '../app/logs')
    # make a directory if it doesn't exist
    assert os.path.exists(logdir) is True

def test_upload_folder():
    '''Searches if the uploads folder exists'''
    response = runner.invoke(create_upload_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    update_dir = os.path.join(root, '../uploads')
    # make a directory if it doesn't exist
    assert os.path.exists(update_dir) is True

def test_upload_file():
    '''Searches if the uploaded file exists'''
    root = os.path.dirname(os.path.abspath(__file__))
    csv_loc = os.path.join(root, '../uploads/transactions.csv')
    csv_file = os.path.exists(csv_loc)
    assert csv_file is False

def test_create_database():
    '''Searches if the database folder exists'''
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) is True
