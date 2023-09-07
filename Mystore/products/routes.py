from flask import Blueprint
from flask import render_template


products = Blueprint('products', __name__)

# FACEBOOK
@products.route('/collections/frontpage')
def facebook():
    return render_template('products/facebook/countries_facebook.html')


@products.route('/products/facebook')
@products.route('/collections/frontpage/products/facebook')
def usa_fb():
    return render_template('products/facebook/usa_fb.html')


@products.route('/collections/frontpage/products/random-country-facebook')
def ran_cn_facebook():
    return render_template('products/facebook/ran_cn_fb.html')


# INSTAGRAM
@products.route('/collections/instagram-account')
def instagram():
    return render_template('products/instagram/instagram_account.html')


@products.route('/products/aged-instagram-without-followers')
@products.route('/collections/instagram-account/products/aged-instagram-without-followers')
def ig_001():
    return render_template('products/instagram/aged_ig_wf_2016.html')


@products.route('/products/aged-instagram-accounts-with-2000-followers')
@products.route('/collections/instagram-account/products/aged-instagram-accounts-with-2000-followers')
def ig_002():
    return render_template('products/instagram/aged_ig_2000.html')


@products.route('/products/instagram-accounts-with-1000-followers')
@products.route('/collections/instagram-account/products/instagram-accounts-with-1000-followers')
def ig_003():
    return render_template('products/instagram/aged_ig_1000.html')

#SNAPCHAT
@products.route('/collections/snapchat-account')
def snapchat():
    return render_template('products/snapchat/snapchat.html')


@products.route('/collections/snapchat-account/products/snapchat-account')
def snap10k():
    return render_template('products/snapchat/snap_10k.html')

#TIKTOK
@products.route('/collections/tiktok-account')
def tiktok():
    return render_template('products/tiktok/tiktok.html')


@products.route('/collections/tiktok-account/products/tiktok-account')
def tik_real():
    return render_template('products/tiktok/tik_1000.html')

#TWITTER
@products.route('/collections/twitter-account')
def twitter():
    return render_template('products/twitter/twitter.html')


@products.route('/collections/twitter-account/products/twitter-account')
def t_without():
    return render_template('products/twitter/t_without.html')

#REDDIT
@products.route('/collections/reddit-account')
def reddit():
    return render_template('products/reddit/reddit.html')

@products.route('/collections/reddit-account/products/aged-reddit')
def aged_reddit():
    return render_template('products/reddit/aged_reddit.html')

@products.route('/collections/reddit-account/products/usa-reddit')
def reddit_karma():
    return render_template('products/reddit/reddit_karma.html')

#LINKEDIN
@products.route('/collections/linkedin-account')
def linkedin():
    return render_template('products/linkedin/linkedin.html')

@products.route('/collections/linkedin-account/products/linkedin-account-with-100-connections')
def link_100():
    return render_template('products/linkedin/link_100.html')
