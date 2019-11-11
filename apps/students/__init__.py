from flask import Blueprint


app_students = Blueprint('students', __name__)
from . import urls
