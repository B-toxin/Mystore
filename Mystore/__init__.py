from flask import Flask
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from Mystore.config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    csrf = CSRFProtect(app)
    db.init_app(app)

    from Mystore.pages.routes import pages
    from Mystore.products.routes import products
    from Mystore.payment.routes import payment

    app.register_blueprint(pages)
    app.register_blueprint(products)
    app.register_blueprint(payment)

    return app
