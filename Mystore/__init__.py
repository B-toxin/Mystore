from flask import Flask


def create_app():
    app = Flask(__name__)
    from Mystore.pages.routes import pages
    from Mystore.products.routes import products
    from Mystore.payment.routes import payments

    app.register_blueprint(pages)
    app.register_blueprint(products)
    app.register_blueprint(payments)

    return app
