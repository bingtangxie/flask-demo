from functools import wraps
from flask import request, url_for, redirect
from apps.models.students import Students


def login_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(request.form)
        if request.form.get('token') != '1':
            return {"status": "unauthorized"}
            # return redirect(url_for('user.login'))         # redirect 只能重定向到GET方法
        return func(*args, **kwargs)
    return wrap


class Auth():
    def authenticate(self, username, password):
        student = Students.query.filter_by(username=username).first()
        if student and student.password == password:
            return student

    def identity(self, payload):
        student_id = payload['identity']
        return Students.get(Students, student_id)