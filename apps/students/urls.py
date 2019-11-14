from apps.students import app_students
from flask_restful import Api
from .views import *


api = Api(app_students)
api.add_resource(StudentsView, '/test')
