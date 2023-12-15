from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended.utils import decode_token
from werkzeug.security import generate_password_hash
from flask import request
from .models import Users, Product
from .db import db


class UserAPI(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]
        decoded_token = decode_token(token)
        if decoded_token:
            user = Users.query.filter_by(public_id=current_user).first()
            return {'username': user.name,
                    "role": user.role,
                    "user_id": current_user,
                    "email": user.email
                    }, 200

        return {"error": "you are not authenticated"}, 401

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        token = request.headers.get("Authorization").split()[1]
        decoded_token = decode_token(token)
        if decoded_token:
            user = Users.query.filter_by(public_id=current_user).first()
            if user.role == "user":
                data = request.get_json()
                orders = data.get("orders")
                for order in orders:
                    product = Product.query.filter_by(public_id=order["product_id"]).first()
                    product.quantity = product.quantity - int(order["quantity"])
                    db.session.commit()

                return {"msg": "success"}, 200
            else:
                return {"err": "you are not authorized"}
        return {"err": "you are not authenticated"}, 401

    @jwt_required()
    def put(self):
        current_user = get_jwt_identity()
        token = request.headers.get("Authorization").split()[1]
        decoded_token = decode_token(token)
        if decoded_token:
            user = Users.query.filter_by(public_id=current_user).first()
            if user.role == "user":
                data = request.get_json()
                username = data.get("username", None)
                email = data.get("email", None)
                password = data.get("password", None)
                print(data)
                if username:
                    user.name = username
                if email:
                    user.email = email
                if password:
                    user.password = generate_password_hash(password)
                db.session.commit()
                return {"msg": "success"}, 200
            else:
                return {"err": "you are not authorized"}
        return {"err": "you are not authenticated"}, 401

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

