from flask import Flask, render_template
from database import db, User
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/user")
def user_list():
    users = User.query.all()
    return render_template("index.html", users=users)


@app.route("/user/<int:id>")
def user_detail(id):
    user = User.query.filter_by(id=id).first()
    return render_template("detail.html", user=user)


if __name__ == "__main__":
    app.run()