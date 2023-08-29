from flask import Blueprint, render_template


pages = Blueprint('pages', __name__)


@pages.route('/')
@pages.route('/home')
def home():
    return render_template('home.html')


@pages.route('/collections/all')
def menu():
    return render_template('menu.html')


@pages.route('/pages/contact')
def contact():
    return render_template('contact.html')


@pages.route('/collections/frontpage')
def facebook():
    return render_template('countries_facebook.html')
