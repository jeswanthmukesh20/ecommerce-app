from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended.utils import decode_token
from flask import request
from .models import Users, Product
import uuid
from .db import db


class ManageProduct(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]
        decoded_token = decode_token(token)
        data = request.get_json()
        if decoded_token:
            product_id = data.get("product_id", None)
            if product_id:
                product = Product.query.filter_by(public_id=product_id).first()
                if product:
                    return {
                        "product_name": product.product_name,
                        "category": product.category,
                        "price": product.price,
                        "quantity": product.quantity,
                        "product_id": product.public_id
                    }
                else:
                    return {"msg": "no product found"}, 404
            else:
                return {"msg": "Product is not found"}, 404

        return {"error": "you are not authenticated"}, 400

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]
        print(token)
        data = request.get_json()
        decoded_token = decode_token(token)
        if decoded_token:
            user = Users.query.filter_by(public_id=current_user).first()
            if user.role == "store manager":
                public_id = str(uuid.uuid4())
                pictures = []
                for picture in data["images"]:
                    pictures.append(picture)

                product = Product(
                    product_name=data["product_name"],
                    quantity=data["quantity"],
                    price=data["price"],
                    category=data["category"],
                    main_image=data["main_image"],
                    images=pictures,
                    public_id=public_id,
                    product_user=user.id
                )
                db.session.add(product)
                db.session.commit()
                return {"msg": "Product added successfully"}, 200
        return {"error": "you are not authenticated"}, 400

    @jwt_required()
    def put(self):
        current_user = get_jwt_identity()
        token = request.headers.get("Authorization").split()[1]
        data = request.get_json()
        decoded_token = decode_token(token)
        if decoded_token:
            product_id = data.get("product_id")
            user = Users.query.filter_by(public_id=current_user).first()
            product = Product.query.filter_by(public_id=product_id).first()
            if product:
                if user.role == "store manager" and product.product_user == user.id:
                    product_name = data.get("product_name", None)
                    quantity = data.get("quantity", None)
                    price = data.get("price", None)
                    category = data.get("category", None)
                    if product_name:
                        product.product_name = product_name
                    if quantity:
                        product.quantity = quantity
                    if price:
                        product.price = price
                    if category:
                        product.category = category
                    db.session.commit()
                    return {"msg": "updated"}, 202
                else:
                    return {"error": "User is not authorized"}, 403
            else:
                return {"error": "product not found"}, 40

        return {"error": "you are not authenticated"}, 401

    @jwt_required()
    def delete(self):
        current_user = get_jwt_identity()
        data = request.get_json()
        token = request.headers.get("Authorization").split()[1]
        decoded_token = decode_token(token)
        product_id = data.get("product_id", None)
        if decoded_token:
            user = Users.query.filter_by(public_id=current_user).first()
            if user.role == "sore manager":
                if product_id:
                    product = Product.query.filter_by(public_id=product_id).first()
                    db.session.delete(product)
                    return {"msg": "delete successfully"}
                else:
                    return {"err": "product not found"}
            else:
                return {"error": "User is not authorized"}, 403

        return {"err": "you are not authorized"}
