from flask import Flask, flash, Blueprint, send_file, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from Mystore import db
import os


app = Flask(__name__)

twi_1000 = Blueprint('twi_1000', __name__)


# Define the Text model
class Text3(db.Model):
    __bind_key__ = 'twi_1000'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class AddTextForm3(FlaskForm):
    text_content3 = TextAreaField('Text Content', validators=[DataRequired()])


@twi_1000.route('/twi_1000_db')
def index3():
    form = AddTextForm3()
    texts = Text3.query.all()
    return render_template('database/twi_1000_db.html', texts=texts, form=form)


@twi_1000.route('/add_text3', methods=['POST'])
def add_text3():
    form = AddTextForm3()
    if form.validate_on_submit():
        text_content3 = form.text_content3.data  # Use 'data' instead of 'content'
        if text_content3:
            new_text = Text3(content=text_content3)  # Use 'content' instead of 'data'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/twi_1000_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/twi_1000_db')


@twi_1000.route('/download_text3')
def download_text3():
    text_to_download = Text3.query.first()
    if text_to_download:
        # Construct the absolute path to the downloaded file
        file_path = os.path.join(app.root_path, 'downloaded_text3.txt')

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


@twi_1000.route('/success/twi_1000', methods=['GET', 'POST'])
def download_after_payment():
    reference_id = request.args.get('reference')

    if is_valid_reference(reference_id):
        # Retrieve the text content from the database
        text_to_download = Text3.query.first()

        if text_to_download:
            # Construct the absolute path to the downloaded file
            file_path = os.path.join(app.root_path, 'downloaded_text3.txt')

            # Create a TXT file and provide it for download
            with open(file_path, 'w') as txt_file:
                txt_file.write(text_to_download.content)

            # Delete the downloaded text from the database
            db.session.delete(text_to_download)
            db.session.commit()

            # Send the file for download
            return send_file(file_path, as_attachment=True)
        else:
            return "No more texts to download."
    else:
        return redirect('https://paystack.com/pay/twi_1000')
