from flask import Blueprint, Flask, render_template

app = Flask(__name__)

pages = Blueprint('pages', __name__)


@pages.route('/')
@pages.route('/home')
def home():
    return render_template('home.html')


@pages.route('/collections/all')
def menu():
    return render_template('menu.html')


@pages.route('/collections')
def catalog():
    return render_template('collections.html')


@pages.route('/pages/contact')
def contact():
    return render_template('contact.html')


@pages.route('/policies/refund-policy')
def refund():
    return render_template('refund_policy.html')


@pages.route('/policies/terms-of-service')
def terms():
    return render_template('terms.html')
