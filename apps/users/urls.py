from flask_restful import Api
from . import app_user
from .views import *


api = Api(app_user)
api.add_resource(LoginView, "/login", endpoint='login')
api.add_resource(RegisterView, "/register")
