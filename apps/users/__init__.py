from flask import Blueprint
from flask_restful import Api
from apps.users.server import User

user_bp = Blueprint('user_bp',__name__)
user_api = Api(user_bp)



user_api.add_resource(User,"/user_get")