from flask_restful import Resource
from ..models.users import Users
from flask_restful import reqparse
from flask_restful import fields
from flask_restful import marshal
from flask import request
from apps import db
from flask_jwt_extended import jwt_required, create_access_token
from datetime import timedelta


parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help="username required")
parser.add_argument('password', type=str, required=True, help="password required")
user_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "password": fields.String
}


class LoginView(Resource):
    # def get(self):
    #     print(request)
    #     args = parser.parse_args()
    #     username = args.get("username")
    #     password = args.get("password")
    #     user = Users.query.filter_by(username=username).first()
    #     if user and user.password == password:
    #         return marshal(user, user_fields)

    def post(self):
        print("request: ", request)
        args = parser.parse_args()
        username = args.get("username")
        password = args.get("password")
        user = Users.query.filter_by(username=username).first()
        if user and user.password == password:
            token = create_access_token(identity=username, expires_delta=timedelta(seconds=30))
            # return marshal(user, user_fields)
            return {
                "message": "success",
                "token": token
            }


class RegisterView(Resource):
    @jwt_required
    def post(self):
        args = parser.parse_args()
        username = args.get("username")
        password = args.get("password")
        user = Users.query.filter_by(username=username).first()
        if not user:
            user = Users()
            user.username = username
            user.password = password

            db.session.add(user)
            db.session.commit()
            return {
                "status": "ok"
            }
        else:
            return {
                "status": "error"
            }
