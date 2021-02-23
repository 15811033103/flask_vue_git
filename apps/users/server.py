from flask import jsonify
from flask_restful import Resource


class User(Resource):

    def get(self):

        return jsonify("ping")