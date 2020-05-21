# 서버의 요청을 처리하는 것들
from flask_restful import Resource
from flask import request


class UserAPI(Resource):
    def get(self, *args, **kwargs):
        return {
            "msg": "hello world!"
        }

    def post(self, *args, **kwargs):
        data = request.get_json()
        name = data.get("name")
        password = data.get("password")
        email = data.get("email")

        return {
            "name": name,
            "password": "secret",
            "email": email
        }
