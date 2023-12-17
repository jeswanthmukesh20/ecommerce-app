from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended.utils import decode_token
from flask import request
from .models import Users, Product, RequestedCategory
import uuid
from werkzeug.utils import secure_filename
from .db import db
from pathlib import Path
import urllib.parse

BASE_DIR = Path("")


class ManageProduct(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        print(current_user)
        token = request.headers.get('Authorization').split()[1]
        decoded_token = decode_token(token)
        if decoded_token:
            user = Users.query.filter_by(public_id=current_user).first()
            products = Product.query.filter_by(product_user=user.id)
            if products:
                products = [{
                    "product_name": product.product_name,
                    "product_id": product.public_id,
                    "quantity": product.quantity,
                    "category": product.category,
                    "price": product.price,
                    "main_image": f"http://localhost:8000/images/{urllib.parse.quote(product.main_image, safe='')}",
                    "images": product.images
                } for product in products]
                print(products)
                return products
            else:
                return {"msg": "no product found"}, 404

        return {"error": "you are not authenticated"}, 400

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]
        data = request.form
        decoded_token = decode_token(token)
        if decoded_token:
            user = Users.query.filter_by(public_id=current_user).first()
            if user.role == "store manager":
                public_id = str(uuid.uuid4())
                pictures = []
                for picture in ["no-picture.jpg" for _ in range(3)]:
                    pictures.append(picture)

                image = request.files.get("product_image", None)
                if image:
                    print(image)
                    destination = (BASE_DIR / 'product_images' / image.filename).as_posix()
                    image.save(destination)

                product_name = data.get("product_name", None)
                image_name = data.get("main_image", None)
                quantity = data.get("quantity", None)
                price = data.get("price", None)
                category = data.get("category", None)

                if  product_name and quantity and price and category:

                    product = Product(
                        product_name=product_name,
                        quantity=quantity,
                        price=price,
                        category=category,
                        main_image=image.filename if not image_name else image_name,
                        images=pictures,
                        public_id=public_id,
                        product_user=user.id
                    )
                    db.session.add(product)

                requested_category = request.form.get("requested_category", None)
                if requested_category:
                    category = RequestedCategory(
                        category_name=requested_category,
                        product_user=user.id
                    )
                    db.session.add(category)
                db.session.commit()
                return {"msg": "Product added successfully"}, 200
        return {"error": "you are not authenticated"}, 400

    @jwt_required()
    def put(self):
        current_user = get_jwt_identity()
        token = request.headers.get("Authorization").split()[1]
        data = request.form
        print(data)
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
                    image_file = request.files.get("product_image", None)
                    if product_name:
                        product.product_name = product_name
                    if quantity:
                        product.quantity = quantity
                    if price:
                        product.price = price
                    if category:
                        product.category = category
                    if image_file:
                        destination = (BASE_DIR / 'product_images' / image_file.filename).as_posix()
                        old_file = BASE_DIR / 'product_images' / product.main_image
                        old_file.unlink(missing_ok=True)
                        product.main_image = image_file.filename
                        image_file.save(destination)
                    db.session.commit()
                    return {"msg": "updated"}, 202
                else:
                    return {"error": "User is not authorized"}, 403
            else:
                return {"error": "product not found"}, 40

        return {"error": "you are not authenticated"}, 401


class DeleteProduct(Resource):
    @jwt_required()
    def post(self):
        print(request.get_json())
        current_user = get_jwt_identity()
        token = request.headers.get("Authorization").split()[1]
        decoded_token = decode_token(token)
        data = request.get_json()
        if decoded_token:
            user = Users.query.filter_by(public_id=current_user).first()
            print(user.name, user.role)
            if user.role == "store manager":
                print(user)
                product_id = data.get("product_id", None)
                if product_id is not None:
                    print(product_id)
                    product = Product.query.filter_by(public_id=product_id).delete()
                    db.session.commit()
                    return {"msg": "delete successfully"}
                else:
                    return {"err": "product not found"}
            else:
                return {"error": "User is not authorized"}, 403

        return {"err": "you are not authorized"}
