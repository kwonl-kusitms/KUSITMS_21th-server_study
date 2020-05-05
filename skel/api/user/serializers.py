from flask_restful import fields


class UserSerializer(object):
    resource_fields = {
        "id": fields.Integer,
        "username": fields.String,
    }
