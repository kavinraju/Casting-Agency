from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
import enum

from .database.models import setup_db

class ErrorMessages(enum.Enum):
    ERROR_400_MESSAGE = "Bad request"
    ERROR_404_MESSAGE = "Resource not found"
    ERROR_405_MESSAGE = "Method not found"
    ERROR_422_MESSAGE = "Uprocessable"

app = Flask(__name__)
setup_db(app)

""" Importing api endpoint from app/api.py """
from .api.api import *