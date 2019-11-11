from flask_restful import Resource
from ..models.students import Students


class StudentsView(Resource):
    def get(self):
        res = Students.query.all()
        print(res)
        return {"msg": "ok"}
