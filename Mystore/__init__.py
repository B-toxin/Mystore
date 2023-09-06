from flask import Flask
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'e71121f8359c7c241f56e489f91f32d7'
    csrf = CSRFProtect(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Replace with your database URL
    db = SQLAlchemy(app)
    from Mystore.pages.routes import pages
    from Mystore.products.routes import products
    from Mystore.payment.routes import payment

    app.register_blueprint(pages)
    app.register_blueprint(products)
    app.register_blueprint(payment)

    return app
