from exceptions import JSONException

from flask import Blueprint, jsonify
from flask_jwt_extended import (
    create_access_token,
    current_user,
    jwt_required,
)
from flask_restful import Api, Resource, marshal_with, reqparse

from apps.user.models import User
from utils import bcrypt

from .user.serializers import UserSerializer


main_api_blueprint = Blueprint("api_main", __name__)
api = Api(main_api_blueprint)


class LoginAPI(Resource):
    @jwt_required
    @marshal_with(UserSerializer.resource_fields)
    def get(self, **kwargs):
        return current_user

    def post(self, **kwargs):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, required=True)
        parser.add_argument("password", type=str, required=True)
        args = parser.parse_args()

        user = User.query.filter_by(username=args.get("username")).first()
        if not user:
            raise JSONException({"msg": "존재하지 않는 유저"}, 404)

        if not bcrypt.check_password_hash(user.password, args.get("password")):
            raise JSONException({"msg": "패스워드가 틀렸습니다."}, 402)

        token = create_access_token(identity=user, fresh=True)
        return jsonify(token=token)


api.add_resource(LoginAPI, "/api/login")
