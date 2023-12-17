from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended.utils import decode_token
from flask import request
from . import Users, Product


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
                "main_image": f"http://localhost:8000/images/{product.main_image}",
                "images": product.images
            } for product in products
        ]
        return products

    # def post(self):
    #     current_user = get_jwt_identity()
    #     token = request.headers.get('Authorization').split()[1]
    #     data = request.form
    #     decoded_token = decode_token(token)
    #     if decoded_token:
    #         user = Users.query.filter_by(public_id=current_user).first()
    #         if user.role == "store manager":
    #             pass