from flask_restful import Api
from api.user import views as user_views


api = Api(prefix="/api")


api.add_resource(user_views.UserListApi, "/user/list")
