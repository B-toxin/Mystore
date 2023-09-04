import requests
from flask import Flask, Blueprint, redirect, render_template, request
from flask_wtf import CSRFProtect
from Mystore.payment.forms import PaymentForm
import time

PAYSTACK_SECRET_KEY = 'sk_live_4471734c006bf88a0ba7494df36e2aaf4d2a60ac'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e71121f8359c7c241f56e489f91f32d7'
csrf = CSRFProtect(app)

payment = Blueprint('payment', __name__)


@payment.route('/checkout', methods=['GET', 'POST'])
def checkout():
    form = PaymentForm()
    if form.validate_on_submit():
        email = form.email.data
        amount = form.amount.data

        # Create a Paystack transaction
        response = create_paystack_transaction(email, amount)
        if response['status']:
            authorization_url = response['data']['authorization_url']
            return redirect(authorization_url)
        else:
            error_message = response['message']
            return render_template('checkout.html', form=form, error_message=error_message)
    return render_template('checkout.html', form=form, error_message=None)


def create_paystack_transaction(email, amount):
    try:
        payload = {
            "email": email,
            "amount": int(amount * 100),  # Convert amount to kobo
            "currency": "NGN",
            "reference": f"paystack_example_{int(time.time())}",
        }
        headers = {
            "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json",
        }

        response = requests.post("https://api.paystack.co/transaction/initialize", json=payload, headers=headers)

        response_data = response.json()
        print(response_data)  # Print the response for inspection

        # Extract the authorization_url from the response_data
        authorization_url = response_data.get("data", {}).get("authorization_url")

        return {"status": True, "authorization_url": authorization_url}
    except Exception as e:
        return {"status": False, "message": str(e)}


@payment.route('/success')
def success():
    status = request.args.get('status')
    file_identifier = request.args.get('file_identifier')  # Extract file identifier from the URL
    if status == 'success':
        # Handle logic for successful payment
        return render_template('success.html', file_identifier=file_identifier)
    else:
        # Handle unauthorized access or other cases
        return redirect('/')

