import os

## Uncomment this while running the test alone.
# This requries you to add a env_file.py file in the environments directory with
# username and password values of you local environment.
#from environments.env_file import *

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True

# DB URI
database_uri = os.environ['DATABASE_URL']
# Local DB Details
#database_name = database_name_env
username = username_env
password = password_env
#local_database_path = "postgresql://{}:{}@{}/{}".format(username, password, 'localhost:5432', database_name)
# Database connection string
SQLALCHEMY_DATABASE_URI = database_uri
# Supress warning
SQLALCHEMY_TRACK_MODIFICATIONS = False


#  Auth0 Credentials used in ./backend/auth/auth.py
AUTH0_DOMAIN_ENV = os.environ['AUTH0_DOMAIN_ENV']
ALGORITHMS_ENV = os.environ['ALGORITHMS_ENV']
API_AUDIENCE_ENV = os.environ['API_AUDIENCE_ENV']

def get_data_base_path(username, password, database_name):
    database_path = "postgresql://{}:{}@{}/{}".format(username, password, 'localhost:5432', database_name)
    return database_path