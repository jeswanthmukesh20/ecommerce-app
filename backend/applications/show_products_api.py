from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended.utils import decode_token
from flask import request
from .models import Users, Product


class ShowProducts(Resource):
    def get(self):
        products = Product.query.all()
        products = [
            {
                "product_name": product.product_name,
                "product_id": product.public_id,
                "quantity": product.quantity,
                "category": product.category,
                "price": product.price,
                "main_image": product.main_image,
                "images": product.images
            } for product in products
        ]
        return products

        # return {"error": "you are not authenticated"}, 401
