import requests
from flask import Flask, Blueprint, redirect, render_template, request, jsonify, session
from flask_wtf import CSRFProtect
from Mystore.payment.forms import PaymentForm
import time

PAYSTACK_SECRET_KEY = 'sk_live_4471734c006bf88a0ba7494df36e2aaf4d2a60ac'
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

        # Generate a unique reference for this payment
        unique_reference = f'paystack_{file_identifier}_{int(time.time())}'

        paystack_data = {
            'key': 'pk_live_8017ced3f46c94721ee3446267b26043297018ff',
            # Replace with your actual public key from Paystack
            'email': form.email.data,
            'amount': amount_in_kobo,
            'currency': 'NGN',
            'ref': unique_reference,  # Use the generated unique reference
            # Add other Paystack parameters as needed
        }

        # Make the payment using Paystack API
        response = requests.post('https://api.paystack.co/transaction/initialize', json=paystack_data)
        payment_data = response.json()

        if payment_data.get('status') and payment_data.get('data').get('status') == 'success':
            # Payment initiation successful, redirect to Paystack payment page
            success_url = f'/success?file_identifier={file_identifier}'
            return redirect(success_url)

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
        session['payment_success'] = True
        return jsonify({'message': 'Payment verified and successful'})
    else:
        # Payment was not successful, handle accordingly
        return jsonify({'message': 'Payment verification failed'})


@payment.route('/verify-payment', methods=['POST'])
def verify_payment():
    data = request.get_json()
    payment_reference = data['reference']

    verify_url = f'https://api.paystack.co/transaction/verify/{payment_reference}'
    headers = {
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}'
    }

    response = requests.get(verify_url, headers=headers)
    verification_data = response.json()

    if verification_data.get('status') and verification_data.get('data').get('status') == 'success':
        # Payment verification successful
        # Update your database or perform other actions here
        return jsonify({'message': 'Payment verified'})
    else:
        # Payment verification failed
        return jsonify({'message': 'Payment verification failed'})


@payment.route('/success')
def success():
    file_identifier = request.args.get('file_identifier')
    payment_success = session.get('payment_success')  # Check if payment was successful
    if payment_success:
        return render_template('success.html', file_identifier=file_identifier)
    else:
        return "Payment not successful."
