from .db import db
from datetime import datetime


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String())
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(300))
    lastseen = db.Column(db.Float())
    email = db.Column(db.String())
    active = db.Column(db.Boolean())
    role = db.Column(db.String())
    user_orders = db.relationship('Orders', backref='users', cascade='all, delete')
    user_address = db.relationship("Address", backref="users", cascade="all, delete")

    def is_admin(self):
        return self.role == "admin"

    def is_store_manager(self):
        return self.role == "store manager"


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    main_image = db.Column(db.String(500), default="no-picture.png")
    images = db.Column(db.PickleType())
    price = db.Column(db.Integer)
    category = db.Column(db.String(50))
    public_id = db.Column(db.String())
    product_user = db.Column(db.Integer, db.ForeignKey(Users.id, ondelete='CASCADE'))


class Orders(db.Model):
    __tablename__ = "Orders"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String())
    user_id = db.Column(db.String(), db.ForeignKey(Users.id, ondelete='CASCADE'))
    product_name = db.Column(db.String())
    quantity = db.Column(db.Integer)
    time = db.Column(db.DateTime, default=datetime.utcnow)


class Address(db.Model):
    __tablename__ = "Address"
    id = db.Column(db.Integer, primary_key=True)
    pincode = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    address_type = db.Column(db.String(20), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey(Users.id, ondelete="CASCADE"))

