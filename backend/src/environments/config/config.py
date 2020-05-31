import os
#from .env_file import database_name_env, heroku_database_uri_env, password_env, username_env 
from environments.env_file import *

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True

# Heroku DB URI
heroku_database_uri = heroku_database_uri_env
# Local DB Details
database_name = database_name_env
username = username_env
password = password_env
local_database_path = "postgresql://{}:{}@{}/{}".format(username, password, 'localhost:5432', database_name)
# Database connection string
SQLALCHEMY_DATABASE_URI = local_database_path
# Supress warning
SQLALCHEMY_TRACK_MODIFICATIONS = False


def get_data_base_path(username, password, database_name):
    database_path = "postgresql://{}:{}@{}/{}".format(username, password, 'localhost:5432', database_name)
    return database_path