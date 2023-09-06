from flask import Flask, Blueprint, send_file, render_template, request, redirect, session
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from Mystore import db
import os


app = Flask(__name__)
# Define a blueprint for payment-related routes
payment = Blueprint('payment', __name__)


# Define the Text model
class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class AddTextForm(FlaskForm):
    text_content = TextAreaField('Text Content', validators=[DataRequired()])


@payment.route('/index')
def index():
    form = AddTextForm()
    texts = Text.query.all()
    return render_template('index.html', texts=texts, form=form)


@payment.route('/add_text', methods=['POST'])
def add_text():
    form = AddTextForm()
    if form.validate_on_submit():
        text_content = form.text_content.data
        if text_content:
            new_text = Text(content=text_content)
            db.session.add(new_text)
            db.session.commit()
    return redirect('/index')


@payment.route('/download_text')
def download_text():
    text_to_download = Text.query.first()
    if text_to_download:
        # Construct the absolute path to the downloaded file
        file_path = os.path.join(app.root_path, 'downloaded_text.txt')

        # Create a TXT file and provide it for download
        with open(file_path, 'w') as txt_file:
            txt_file.write(text_to_download.content)

        # Delete the downloaded text from the database
        db.session.delete(text_to_download)
        db.session.commit()

        return send_file(file_path, as_attachment=True)
    else:
        return "No more texts to download."


# Function to check if the reference ID is valid (e.g., in a database)
def is_valid_reference(reference_id):
    return reference_id is not None


@payment.route('/success/ran_fb')
def ran_fb():
    reference_id = request.args.get('reference')
    if is_valid_reference(reference_id):
        return render_template('success/success_ran_fb.html')
    else:
        return redirect('https://paystack.com/pay/ran_fb')


@payment.route('/success/r_fb', methods=['GET', 'POST'])
def r_fb():
    form = AddTextForm()  # Create an instance of your form
    return render_template('download_ran_fb.html', form=form)


@payment.route('/success/usa_fb')
def usa_fb():
    reference_id = request.args.get('reference')
    if is_valid_reference(reference_id):
        session['downloaded'] = True
        return render_template('success/success_usa_fb.html')
    else:
        return redirect('https://paystack.com/pay/usa_fb')
