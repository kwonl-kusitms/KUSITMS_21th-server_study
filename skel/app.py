from exceptions import HTTPException, JSONException, errohandler

from flask import Flask

from api.endpoints import api
from apps.user.views import user_blueprint
from apps.views import main_blueprint
from database import db, migrate
from settings import Config
from utils import bcrypt, jwt


app = Flask(__name__)

"""General app config"""
app.config.from_object(Config)
app.url_map.strict_slashes = False

"""Third party configuration"""
db.init_app(app)
api.init_app(app)
migrate.init_app(app, db)
bcrypt.init_app(app)
jwt.init_app(app)

"""Blueprint registration"""
app.register_blueprint(main_blueprint)
app.register_blueprint(user_blueprint)

"""Error handler"""
app.errorhandler(HTTPException)(errohandler)
app.errorhandler(JSONException)(errohandler)
