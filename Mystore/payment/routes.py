from flask import Flask, Blueprint, render_template, request
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e71121f8359c7c241f56e489f91f32d7'
csrf = CSRFProtect(app)

payment = Blueprint('payment', __name__)


@payment.route('/success')
def success():
    file_identifier = request.args.get('file_identifier')
    # Additional logic may be needed here
    return render_template('success.html', file_identifier=file_identifier)
