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

    # Configure multiple database bindings
    app.config['SQLALCHEMY_BINDS'] = {
        'text_database': app.config['SQLALCHEMY_DATABASE_URI'],
        'usa_fb': app.config['SQLALCHEMY_BINDS']['usa_fb'],
        'tik_1000': app.config['SQLALCHEMY_BINDS']['tik_1000'],
        'twi_1000': app.config['SQLALCHEMY_BINDS']['twi_1000'],
        'twi_2016_2009': app.config['SQLALCHEMY_BINDS']['twi_2016_2009'],
        'ig_f_2018_2016': app.config['SQLALCHEMY_BINDS']['ig_f_2018_2016']
    }

    from Mystore.usa_fb.routes import usa_fb
    from Mystore.pages.routes import pages
    from Mystore.products.routes import products
    from Mystore.ran_fb.routes import ran_fb
    from Mystore.tik_1000.routes import tik_1000
    from Mystore.twi_1000.routes import twi_1000
    from Mystore.twi_2016_2009.routes import twi_2016_2009
    from Mystore.ig_f_2018_2016.routes import ig_f_2018_2016

    app.register_blueprint(ig_f_2018_2016)
    app.register_blueprint(twi_2016_2009)
    app.register_blueprint(twi_1000)
    app.register_blueprint(tik_1000)
    app.register_blueprint(pages)
    app.register_blueprint(products)
    app.register_blueprint(ran_fb)
    app.register_blueprint(usa_fb)

    return app
