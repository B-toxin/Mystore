from flask import Blueprint
from flask import render_template


products = Blueprint('products', __name__)

# FACEBOOK
@products.route('/collections/frontpage/products/uk-facebook')
def uk_facebook():
    return render_template('products/facebook/uk_facebook.html')


@products.route('/collections/frontpage/products/facebook')
def usa_fb():
    return render_template('products/facebook/usa_fb.html')


@products.route('/collections/frontpage/products/canada-facebook-with-real-friends')
def canada_facebook():
    return render_template('products/facebook/canada_fb.html')


@products.route('/collections/frontpage/products/germany-facbook')
def germany_facebook():
    return render_template('products/facebook/germany_fb.html')

# INSTAGRAM
@products.route('/collections/instagram-account/products/copy-of-aged-instagram-without-followers')
def ig_001():
    return render_template('products/instagram/test_aged_ig_without_f.html')
