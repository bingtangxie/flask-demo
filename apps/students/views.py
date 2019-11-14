from flask_restful import Resource, fields, marshal
from ..models.students import Students
from flask_restful import reqparse
from apps.utils import login_required
from flask_jwt_extended import jwt_required


parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="Please input arg 'name'")
parser.add_argument("age", type=int, required=True, help="Please input arg 'age'")


resource_fields = {
    'id': fields.Integer,
    'name': fields.String
}


class StudentsView(Resource):
    # 视图类装饰器
    # method_decorators = [login_required]
    @jwt_required
    def get(self):
        # GET/POST参数的验证
        args = parser.parse_args()
        name = args.get("name")
        age = args.get("age")
        res = Students.query.all()
        # 对象数据序列化
        return {"msg": "ok", "data": marshal(res, resource_fields)}
