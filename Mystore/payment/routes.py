from flask import Flask, Blueprint, render_template, request
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e71121f8359c7c241f56e489f91f32d7'
csrf = CSRFProtect(app)

payment = Blueprint('payment', __name__)


@payment.route('/success/usa_fb')
def success():
    return render_template('success_usa_fb.html')


@payment.route('/success/ran_fb')
def success():
    return render_template('success_ran_fb.html')
