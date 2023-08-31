from flask import Blueprint
from flask import render_template


products = Blueprint('products', __name__)

# FACEBOOK
@products.route('/collections/frontpage/products/facebook')
def usa_fb():
    return render_template('products/facebook/usa_fb.html')


@products.route('/collections/frontpage/products/random-country-facebook')
def ran_cn_facebook():
    return render_template('products/facebook/ran_cn_fb.html')


# INSTAGRAM
@products.route('/collections/instagram-account/products/copy-of-aged-instagram-without-followers')
def ig_001():
    return render_template('products/instagram/aged_ig_wf_2016.html')
