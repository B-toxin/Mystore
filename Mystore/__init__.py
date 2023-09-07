from flask import Flask
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from Mystore.config import Config
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    csrf = CSRFProtect(app)
    db.init_app(app)
    migrate = Migrate(app, db)

    # Configure multiple database bindings
    app.config['SQLALCHEMY_BINDS'] = {
        'text_database': app.config['SQLALCHEMY_DATABASE_URI'],
        'usa_fb': app.config['SQLALCHEMY_BINDS']['usa_fb']  # Use the correct key here
    }

    from Mystore.usa_fb.routes import usa_fb
    from Mystore.pages.routes import pages
    from Mystore.products.routes import products
    from Mystore.ran_fb.routes import ran_fb

    app.register_blueprint(pages)
    app.register_blueprint(products)
    app.register_blueprint(ran_fb)
    app.register_blueprint(usa_fb)

    return app
