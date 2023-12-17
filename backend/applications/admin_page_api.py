from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended.utils import decode_token
from flask import request
from .models import Users, RequestedCategory
import uuid
from werkzeug.utils import secure_filename
from .db import db
from pathlib import Path
import urllib.parse


class Admin(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        print(current_user)
        token = request.headers.get('Authorization').split()[1]
        decoded_token = decode_token(token)
        if decoded_token:
            user = Users.query.filter_by(public_id=current_user).first()
            if user.role == "admin":
                managers = [
                    {
                        "user_id": usr.public_id,
                        "username": usr.name,
                        "email": usr.email,
                        "role": "store manager"
                    }
                    for usr in Users.query.filter_by(role="store manager")
                ]
                users = [{
                    "user_id": usr.public_id,
                    "username": usr.name,
                    "email": usr.email,
                    "role": "user"
                }
                    for usr in Users.query.filter_by(role="user")
                ]
                users.extend(managers)
                return users
        return {"error": "you are not authenticated"}, 400

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]
        decoded_token = decode_token(token)
        if decoded_token:
            user = Users.query.filter_by(public_id=current_user).first()
            if user.role == "admin":
                data = request.get_json()
                user_id = data.get("user_id", None)
                if user_id:
                    user = Users.query.filter_by(public_id=user_id).delete()
                    db.session.commit()
                    return {"msg": "deleted successfully"}
                else:
                    return {"err": "enter valid input"}

        return {"err": "you are not authenticated"}


class Category(Resource):

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]
        decoded_token = decode_token(token)
        if decoded_token:
            user = Users.query.filter_by(public_id=current_user).first()
            if user.role == "admin":
                categories = RequestedCategory.query.join(Users, RequestedCategory.product_user == Users.id)
                categories = [
                    {
                        "category_name": category.category_name,
                        "username": Users.query.filter_by(id=category.product_user).first().name,
                        "status": category.approved,
                        "id": category.id
                    }
                    for category in categories
                ]
                return categories
        return {"err": "you are not authenticated"}

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]
        decoded_token = decode_token(token)
        if decoded_token:
            user = Users.query.filter_by(public_id=current_user).first()
            if user.role == "admin":
                data = request.get_json()
                category_id = data.get("category_id")
                category = RequestedCategory.query.filter_by(id=category_id).first()
                category.approved = True
                db.session.commit()
                return {"message": "successful"}
        return {"err": "you are not authenticated"}
