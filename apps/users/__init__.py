from flask import Blueprint


app_user = Blueprint("user", __name__)
from . import urls
