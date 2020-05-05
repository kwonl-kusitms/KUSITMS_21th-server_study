from flask import Blueprint
from flask_restful import Api, Resource, marshal_with, reqparse
from sqlalchemy.exc import IntegrityError
from exceptions import JSONException

from apps.user.models import User
from database import db

from .serializers import UserSerializer
from utils import bcrypt


user_api_blueprint = Blueprint("api_user", __name__, url_prefix="/api/user")
api = Api(user_api_blueprint)


class UserListApi(Resource):
    @marshal_with(UserSerializer.resource_fields)
    def get(self, **kwargs):
        return User.query.all()

    @marshal_with(UserSerializer.resource_fields)
    def post(self, **kwargs):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, required=True)
        parser.add_argument("password", type=str, required=True)
        args = parser.parse_args()

        password_hash = bcrypt.generate_password_hash(
            args.get("password")
        ).decode()

        try:
            user = User(username=args.get("username"), password=password_hash)
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            raise JSONException({"message": "유저가 이미 존재합니다."}, 409)

        return user


api.add_resource(UserListApi, "")
