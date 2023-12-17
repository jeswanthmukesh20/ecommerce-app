from flask_restful import Resource
from . import Product, RequestedCategory


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
        categories = RequestedCategory.query.filter_by(approved=True).all()
        categories = [
            category.category_name for category in categories
        ]
        return {"products": products, "categories": categories}
