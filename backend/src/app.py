from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json

from .database.models import setup_db

app = Flask(__name__)
setup_db(app)

""" Importing api endpoint from app/api.py """
from .api.api import *