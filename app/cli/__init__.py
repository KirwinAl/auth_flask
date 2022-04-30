import os

import click
from flask.cli import with_appcontext
from app.db import db

@click.command(name='create-db')
@with_appcontext
def create_database():
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../../database')
    # make a directory if it doesn't exist
    if not os.path.exists(dbdir):
        os.mkdir(dbdir)
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

@click.command(name='create-log-folder')
@with_appcontext
def create_log_folder():
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, '../logs')
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)