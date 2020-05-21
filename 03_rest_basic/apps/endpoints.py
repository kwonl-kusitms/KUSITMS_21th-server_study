from flask_restful import Api
from apps.user.views import UserAPI


api = Api()

api.add_resource(UserAPI, "/user")
