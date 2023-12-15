from flask import Flask
from flask import jsonify
from flask import request
from flask_restful import Api
from werkzeug.security import generate_password_hash, check_password_hash
from flask import send_from_directory

from applications import db
from applications.models import Users
from applications.show_products_api import ShowProducts
from applications.user_api import UserAPI
from applications import ManageProduct, DeleteProduct, BASE_DIR
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager
import time
import uuid

app = Flask(__name__)
print(BASE_DIR.absolute())
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
api = Api(app)
db.init_app(app)
cors = CORS(app)
jwt = JWTManager(app)
with app.app_context():
    db.create_all()

roles = {
    "manager": "store manager",
    "user": "user",
    "admin": "admin"
}


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    print(data)
    username = data.get("username", None)
    password = data.get("password", None)
    if "@" in username:
        user = Users.query.filter_by(email=username).first()
    else:
        print("username")
        user = Users.query.filter_by(name=username).first()
    print(user)
    if user and check_password_hash(user.password, password):
        user.lastseen = time.time()
        db.session.commit()
        access_token = create_access_token(identity=user.public_id, additional_claims={'role': user.role})
        return jsonify({
            'access_token': access_token,
            'username': user.name,
            'role': user.role,
            'user_id': user.public_id,
            'email': user.email
        }), 200

    return jsonify({'error': 'Invalid credentials'}), 403


@app.route('/images/<path>', methods=["GET"])
def send_report(path):
    print(path)
    return send_from_directory('product_images', path)


@app.route("/register/<user_type>", methods=["POST"])
def signup(user_type):
    print(user_type)
    role = roles.get(user_type, None)
    if role is None:
        return {"error": "role not found"}, 404
    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)
    email = data.get("email", None)
    user = Users.query.filter_by(email=data['email']).first()
    if user:
        return {"error": "email id already exists"}, 409

    if email and password:
        hashed_password = generate_password_hash(password)
        public_id = str(uuid.uuid4())
        new_user = Users(
            public_id=public_id,
            name=username,
            password=hashed_password,
            role=role,
            email=email,
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': f'{role} registered successfully'}), 201
    return {"error": "Insufficient credentials"}, 400


api.add_resource(ShowProducts, "/shop")
api.add_resource(ManageProduct, "/manage_product")
api.add_resource(DeleteProduct, "/delete_product")
api.add_resource(UserAPI, "/user_actions")

if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True, host="0.0.0.0", port=8000)
