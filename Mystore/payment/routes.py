from flask import Blueprint, redirect
from flask import render_template, url_for, request
PAYSTACK_SECRET_KEY = 'sk_test_2dc84a4699b7125060e892773bebfecb47190ee6'


payments = Blueprint('payments', __name__)


@payments.route('/checkout/<file_identifier>')
def checkout(file_identifier):
    # Use the file identifier to customize the payment form for the specific file
    return render_template('payment.html', file_identifier=file_identifier)


@payments.route('/process_payment/<file_identifier>', methods=['GET', 'POST'])
def process_payment(file_identifier):
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        amount = request.form.get('amount')

        # Process the payment and other necessary steps
        # Redirect to the success page after successful payment
        return redirect(url_for('.success', file_identifier=file_identifier))

        # Handle GET request if needed
        # For example, render the payment form template
    return render_template('payment.html', file_identifier=file_identifier)


@payments.route('/success/<file_identifier>')
def success(file_identifier):
    print(file_identifier)
    # Retrieve file details from the database based on file_identifier
    # Display success message and provide a link to download
    return render_template('success_page.html', file_identifier=file_identifier)
