from flask import Flask, Blueprint, render_template, request, redirect, url_for
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e71121f8359c7c241f56e489f91f32d7'
csrf = CSRFProtect(app)

payment = Blueprint('payment', __name__)


@payment.route('/success/usa_fb')
def usa_fb():
    reference_id = request.args.get('reference')

    # Check if the reference ID is valid (e.g., in a database)
    if is_valid_reference(reference_id):
        return render_template('success/success_usa_fb.html')
    else:
        # Redirect or display an error message for invalid reference IDs
        return redirect('https://paystack.com/pay/usa_fb')


def is_valid_reference(reference_id):
    return reference_id is not None
