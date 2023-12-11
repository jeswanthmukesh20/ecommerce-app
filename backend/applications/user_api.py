from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended.utils import decode_token
from flask import request
from .models import Users


class UserAPI(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]
        decoded_token = decode_token(token)
        if decoded_token:
            user = Users.query.filter_by(public_id=current_user).first()
            return {'message': "You are Logged in", 'username': user.name,
                    "role": user.role,
                    "user_id": current_user,
                    }, 200

        return {"error": "you are not authenticated"}, 401

    # @jwt_required()
    # def post(self):
    #     current_user = get_jwt_identity()
    #     token = request.headers.get("Authorization").split()[1]
    #     decoded_token = decode_token(token)
    #     data = request.get_json()
    #     if decoded_token:
    #         user = Users.query.filter_by(public_id=current_user).first()
    #         if data[""]
    #

