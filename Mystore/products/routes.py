from flask import Flask, Blueprint, render_template, flash

app = Flask(__name__)
app.secret_key = 'e71121f8359c7c241f56e489f91f32d7'

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
@products.route('/products/random-country-facebook')
def ran_cn_facebook():
    return render_template('products/facebook/ran_cn_fb.html')
@products.route('/collections/frontpage/products/copy-of-usa-facebook-with-real-friends')
@products.route('/collections/all/products/copy-of-usa-facebook-with-real-friends')
def usa_date_facebook():
    return render_template('products/facebook/usa_dating_fb.html')
@products.route('/collections/frontpage/products/copy-of-usa-dating-facebook')
@products.route('/collections/all/products/copy-of-usa-dating-facebook')
def uk_facebook():
    return render_template('products/facebook/uk_fb.html')
@products.route('/collections/frontpage/products/copy-of-uk-country-facebook')
@products.route('/collections/all/products/copy-of-uk-country-facebook')
def cn_facebook():
    return render_template('products/facebook/canada_fb.html')

# INSTAGRAM
@products.route('/collections/instagram-account')
def instagram():
    return render_template('products/instagram/instagram_account.html')
@products.route('/collections/all/products/copy-of-2018-2016-instagram-without-followers')
@products.route('/collections/instagram-account/products/copy-of-2018-2016-instagram-without-followers')
@products.route('/products/copy-of-2018-2016-instagram-without-followers')
def ig_001():
    return render_template('products/instagram/ig_po_2020_2012.html')
@products.route('/collections/all/products/aged-instagram-accounts-with-2000-followers')
@products.route('/collections/instagram-account/products/aged-instagram-accounts-with-2000-followers')
@products.route('/products/aged-instagram-accounts-with-2000-followers')
def ig_002():
    return render_template('products/instagram/ig_2000f_2018_2016.html')
@products.route('/collections/all/products/instagram-accounts-with-1000-followers')
@products.route('/collections/instagram-account/products/instagram-accounts-with-1000-followers')
@products.route('/products/instagram-accounts-with-1000-followers')
def ig_003():
    return render_template('products/instagram/ig_1000f_2018_2016.html')
@products.route('/collections/all/products/aged-instagram-without-followers')
@products.route('/products/aged-instagram-without-followers')
@products.route('/collections/instagram-account/products/aged-instagram-without-followers')
def ig_004():
    return render_template('products/instagram/ig_f_2018_2016.html')

#SNAPCHAT
@products.route('/collections/snapchat-account')
def snapchat():
    return render_template('products/snapchat/snapchat.html')
@products.route('/collections/snapchat-account/products/snapchat-account')
@products.route('/collections/all/products/snapchat-account')
def snap10k():
    return render_template('products/snapchat/snap_10k.html')
@products.route('/collections/snapchat-account/products/copy-of-snapchat-account-with-100k-snapscore')
@products.route('/collections/all/products/copy-of-snapchat-account-with-100k-snapscore')
def snap50k():
    return render_template('products/snapchat/snap_50k.html')
@products.route('/collections/snapchat-account/products/snapchat-account-with-100k-snapscore')
@products.route('/collections/all/products/snapchat-account-with-100k-snapscore')
def snap100k():
    return render_template('products/snapchat/snap_100k.html')

#TIKTOK
@products.route('/collections/tiktok-account')
def tiktok():
    return render_template('products/tiktok/tiktok.html')
@products.route('/collections/tiktok-account/products/tiktok-account')
@products.route('/collections/all/products/tiktok-account')
def tik_1000():
    return render_template('products/tiktok/tik_1000.html')
@products.route('/collections/tiktok-account/products/tiktok-account-with-1000-followers')
@products.route('/collections/all/products/tiktok-account-with-1000-followers')
def tik_4000():
    return render_template('products/tiktok/tik_4000.html')

#TWITTER
@products.route('/collections/twitter-account')
def twitter():
    return render_template('products/twitter/twitter.html')
@products.route('/collections/twitter-account/products/copy-of-twitter-account-without-followers')
@products.route('/collections/all/products/copy-of-twitter-account-without-followers')
def t_1000():
    return render_template('products/twitter/twi_1000.html')
@products.route('/collections/twitter-account/products/twitter-account')
@products.route('/collections/all/products/twitter-account')
def t_2016():
    return render_template('products/twitter/twi_2016_2009.html')

#REDDIT
@products.route('/collections/reddit-account')
def reddit():
    return render_template('products/reddit/reddit.html')

@products.route('/collections/reddit-account/products/aged-reddit')
@products.route('/collections/all/products/aged-reddit')
def aged_reddit():
    return render_template('products/reddit/aged_reddit.html')

@products.route('/collections/reddit-account/products/usa-reddit')
@products.route('/collections/all/products/usa-reddit')
def reddit_karma():
    return render_template('products/reddit/reddit_1000_karma.html')

#LINKEDIN
@products.route('/collections/linkedin-account')
def linkedin():
    return render_template('products/linkedin/linkedin.html')
@products.route('/collections/linkedin-account/products/linkedin-account')
@products.route('/collections/all/products/linkedin-account')
def link():
    return render_template('products/linkedin/link.html')
@products.route('/collections/linkedin-account/products/linkedin-account-with-100-connections')
@products.route('/collections/all/products/linkedin-account-with-100-connections')
def link_100():
    return render_template('products/linkedin/link_100.html')
@products.route('/collections/linkedin-account/products/copy-of-linkedin-account-with-100-connections')
@products.route('/collections/all/products/copy-of-linkedin-account-with-100-connections')
def link_200():
    return render_template('products/linkedin/link_200.html')
@products.route('/collections/linkedin-account/products/linkedin-account-with-500-connections')
@products.route('/collections/all/products/linkedin-account-with-500-connections')
def link_500():
    return render_template('products/linkedin/link_500.html')

#GOOGLE VOICE
@products.route('/collections/google-voice')
def gv():
    return render_template('products/Google Voice/gv.html')
@products.route('/collections/google-voice/products/google-voice-usa')
@products.route('/collections/all/products/google-voice-usa')
def gv_usa():
    return render_template('products/Google Voice/gv_usa.html')
