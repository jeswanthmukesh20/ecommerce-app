from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_restful import Api
from werkzeug.security import generate_password_hash, check_password_hash
from flask import send_from_directory
from functools import wraps
from applications import db
from applications.models import Users, Orders
from applications.show_products_api import ShowProducts
from applications.user_api import UserAPI
from applications.admin_page_api import Admin, Category
from applications import ManageProduct, DeleteProduct
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager
import time
import uuid
from flask_caching import Cache
from datetime import timedelta, datetime
from celery import Celery, Task
from flask_mail import Mail, Message
from celery.schedules import crontab

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
app.config["CACHE_TYPE"] = "redis"
app.config["CACHE_REDIS_HOST"] = "localhost"
app.config["CACHE_REDIS_PORT"] = "6379"
app.config["CACHE_REDIS_DB"] = "0"
app.config["CACHE_REDIS_URL"] = "redis://localhost:6379/0"
app.config["CACHE_DEFAULT_TIMEOUT"] = "500"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ["EMAIL"]
app.config['MAIL_PASSWORD'] = os.environ["PASSWORD"]
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config["MAIL_INTERVAL"] = 24
mail = Mail(app)


def make_celery(app):
    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
    celery = Celery(app.name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)

    class ContextTask(Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.test_request_context() as g:
                g.in_celery_task = True
                res = self.run(*args, **kwargs)
                return res

    celery.Task = ContextTask
    celery.config_from_object(__name__)
    celery.conf.timezone = 'UTC'
    return celery


celery = make_celery(app)

api = Api(app)
db.init_app(app)
cors = CORS(app)
jwt = JWTManager(app)
cache = Cache(app)
with app.app_context():
    db.create_all()

app.logger.info("starting new app")

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
# @cache.cached(timeout=50)
def send_image(path):
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


def cached_decoratory(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_function = cache.cached(timeout=50)(func)
        return cache_function(*args, **kwargs)

    return wrapper


ShowProducts.get = cached_decoratory(ShowProducts.get)

api.add_resource(ShowProducts, "/shop")
api.add_resource(ManageProduct, "/manage_product")
api.add_resource(DeleteProduct, "/delete_product")
api.add_resource(UserAPI, "/user_actions")
api.add_resource(Admin, "/admin")
api.add_resource(Category, "/admin/category")


@celery.task
def send_message():
    users = Users.query.filter_by(role="user").all()
    mail_users = []
    mails = []
    for user in users:
        timestamp = datetime.fromtimestamp(user.lastseen)
        current_datetime = datetime.now()
        time_difference = current_datetime - timestamp
        hours_difference = time_difference.seconds // 3600
        if hours_difference >= app.config["MAIL_INTERVAL"]:
            mail_users.append((user.name, user.email))
            mails.append(user.email)
    for username, email in mail_users:
        email_content = render_template(
            template_name_or_list='Mail.html',
            recipient=username,
            sender=app.config["MAIL_USERNAME"],
            website_name="KiranaKart"
        )
        msg = Message(
            subject='We Miss You! Come Back and Explore More',
            recipients=[email],
            sender=app.config["MAIL_USERNAME"]
        )
        msg.html = email_content
        mail.send(msg)


@celery.task
def send_monthly_report():
    users = Users.query.filter_by(role="user").all()
    for user in users:
        orders = Orders.query.filter_by(user_id=user.id).all()
        total_amount_spent = 0
        current_time = datetime.utcnow()
        for order in orders:
            order_time = order.time
            time_difference = (current_time - order_time).days
            if time_difference <= 30:
                total_amount_spent += order.total_cost
        email_content = render_template(
            'MonthlyReport.html',
            total_spent=total_amount_spent,
            username=user.name,
            year=current_time.year,
            month=current_time.month
        )
        msg = Message(
            subject='Your Monthly Order Report',
            sender=app.config["MAIL_USERNAME"],
            recipients=[user.email]
        )
        msg.html = email_content
        mail.send(msg)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=17, minute=30),
        send_message.s(),
        name='Send Mail Everyday')
    sender.add_periodic_task(
        crontab(hour=0, minute=0, day_of_month="1"),
        send_monthly_report.s(),
        name="Send Monthly Report"
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
