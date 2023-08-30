import requests
from flask import Flask, Blueprint, redirect, render_template, request, jsonify
from flask_wtf import CSRFProtect
from Mystore.payment.forms import PaymentForm
import time

PAYSTACK_SECRET_KEY = 'sk_test_2dc84a4699b7125060e892773bebfecb47190ee6'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e71121f8359c7c241f56e489f91f32d7'
csrf = CSRFProtect(app)

payment = Blueprint('payment', __name__)


@payment.route("/checkout", methods=['GET', 'POST'])
def checkout():
    file_identifier = request.args.get('file_identifier')
    form = PaymentForm()

    if form.validate_on_submit():
        amount_in_kobo = int(form.amount.data * 100)  # Convert NGN to kobo
        paystack_data = {
            'key': 'pk_test_60a3e1f9abc3bbe710308289a796d2e7b6f428ad',
            'email': form.email.data,
            'amount': amount_in_kobo,
            'currency': 'NGN',
            'ref': f'paystack_example_{int(time.time())}',
            # Add other Paystack parameters as needed
        }

        # Make the payment using Paystack API
        response = requests.post('https://api.paystack.co/transaction/initialize', json=paystack_data)
        payment_data = response.json()

        if payment_data.get('status') and payment_data.get('data').get('status') == 'success':
            # Payment initiation successful, redirect to Paystack payment page
            return redirect(payment_data.get('data').get('authorization_url'))

        # Payment initiation failed, handle the error accordingly

    return render_template('checkout.html', form=form, file_identifier=file_identifier)


@payment.route('/payment/callback', methods=['POST'])
def payment_callback():
    event = request.json
    payment_reference = event['data']['reference']
    verify_url = f'https://api.paystack.co/transaction/verify/{payment_reference}'
    headers = {
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}'
    }
    response = requests.get(verify_url, headers=headers)
    data = response.json()

    if data['status'] and data['data']['status'] == 'success':
        # Payment was successful, verify the payment details
        amount_paid = data['data']['amount'] / 100  # Convert amount from kobo to NGN
        email = data['data']['customer']['email']

        # You can update your database or perform other actions here
        return jsonify({'message': 'Payment verified and successful'})
    else:
        # Payment was not successful, handle accordingly
        return jsonify({'message': 'Payment verification failed'})


@payment.route('/success/<file_identifier>')
def success(file_identifier):
    return render_template('success.html', file_identifier=file_identifier)
