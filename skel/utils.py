from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from apps.user.models import User


bcrypt = Bcrypt()


jwt = JWTManager()


@jwt.user_loader_callback_loader
def jwt_identity(payload):
    return User.query.get(payload)


@jwt.user_identity_loader
def identity_loader(user):
    return user.id
