'''Testing for files and directories'''
import os
from click.testing import CliRunner
from app import create_log_folder, create_database
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
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    update_dir = os.path.join(root, '../uploads')
    # make a directory if it doesn't exist
    assert os.path.exists(update_dir) is True

def test_upload_file():
    '''Searches if the uploaded file exists'''
    root = os.path.dirname(os.path.abspath(__file__))
    csv_loc = os.path.join(root, '../uploads/music.csv')
    csv_file = os.path.exists(csv_loc)
    assert csv_file is False

def test_error_log_file():
    '''Searches if the error log file exists'''
    root = os.path.dirname(os.path.abspath(__file__))
    error_log = os.path.join(root, '../app/logs/errors.log')
    logfile = os.path.exists(error_log)
    assert logfile is True

def test_flask_log_file():
    '''Searches if the flask log file exists'''
    root = os.path.dirname(os.path.abspath(__file__))
    flask_log = os.path.join(root, '../app/logs/flask.log')
    logfile = os.path.exists(flask_log)
    assert logfile is True

def test_myapp_log_file():
    '''Searches if the myApp log file exists'''
    root = os.path.dirname(os.path.abspath(__file__))
    myapp_log = os.path.join(root, '../app/logs/myapp.log')
    logfile = os.path.exists(myapp_log)
    assert logfile is True

def test_request_log_file():
    '''Searches if the request log file exists'''
    root = os.path.dirname(os.path.abspath(__file__))
    request_log = os.path.join(root, '../app/logs/request.log')
    logfile = os.path.exists(request_log)
    assert logfile is True

def test_sql_log_file():
    '''Searches if the sql log file exists'''
    root = os.path.dirname(os.path.abspath(__file__))
    sql_log = os.path.join(root, '../app/logs/sqlalchemy.log')
    logfile = os.path.exists(sql_log)
    assert logfile is True

def test_werk_log_file():
    '''Searches if the werkzeug log file exists'''
    root = os.path.dirname(os.path.abspath(__file__))
    werk_log = os.path.join(root, '../app/logs/werkzeug.log')
    logfile = os.path.exists(werk_log)
    assert logfile is True

def test_create_database():
    '''Searches if the database folder exists'''
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) is True
