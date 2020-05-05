from flask import Blueprint, Response, render_template
from .models import User
from exceptions import HTTPException


user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.route("", methods=["GET"])
def get_user_list():
    users = User.query.all()

    return render_template("user/list.html", users=users)


@user_blueprint.route("/<int:id>", methods=["GET"])
def get_user_detail(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        raise HTTPException("user not found", 404)

    return Response(
        f"Your name is: {user.username} and password is {user.password}"
    )
