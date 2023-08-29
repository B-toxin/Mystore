from flask import Blueprint
from flask import render_template


products = Blueprint('products', __name__)


@products.route('/collections/frontpage/products/uk-facebook')
def uk_facebook():
    return render_template('products/uk_facebook.html')


@products.route('/collections/frontpage/products/facebook')
def usa_fb():
    return render_template('products/usa_fb.html')


@products.route('/collections/frontpage/products/canada-facebook-with-real-friends')
def canada_facebook():
    return render_template('products/canada_fb.html')


@products.route('/collections/frontpage/products/germany-facbook')
def germany_facebook():
    return render_template('products/germany_fb.html')
