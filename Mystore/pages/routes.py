from flask import Blueprint, Flask, render_template, request

app = Flask(__name__)

pages = Blueprint('pages', __name__)


@pages.route('/')
@pages.route('/home')
def home():
    return render_template('pages/home.html')


@pages.route('/collections')
def catalog():
    return render_template('pages/collections.html')


@pages.route('/collections/all')
def menu():
    page_number = request.args.get('page', default=1, type=int)

    if page_number == 2:
        return render_template('pages/menu_1.html')
    else:
        return render_template('pages/menu.html')


@pages.route('/pages/contact')
def contact():
    return render_template('pages/contact.html')


@pages.route('/policies/refund-policy')
def refund():
    return render_template('pages/refund_policy.html')


@pages.route('/policies/terms-of-service')
def terms():
    return render_template('pages/terms.html')
