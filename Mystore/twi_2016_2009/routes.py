from flask import Flask, flash, Blueprint, send_file, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from Mystore import db
import os


app = Flask(__name__)

twi_2016_2009 = Blueprint('twi_2016_2009', __name__)


# Define the Text model
class Text4(db.Model):
    __bind_key__ = 'twi_2016_2009'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class AddTextForm4(FlaskForm):
    text_content4 = TextAreaField('Text Content', validators=[DataRequired()])


@twi_2016_2009.route('/twi_2016_2009_db')
def index4():
    form = AddTextForm4()
    texts = Text4.query.all()
    return render_template('database/twi_2016_2009_db.html', texts=texts, form=form)


@twi_2016_2009.route('/add_text4', methods=['POST'])
def add_text4():
    form = AddTextForm4()
    if form.validate_on_submit():
        text_content4 = form.text_content4.data  # Use 'data' instead of 'content'
        if text_content4:
            new_text = Text4(content=text_content4)  # Use 'content' instead of 'data'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/twi_2016_2009_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/twi_2016_2009_db')


@twi_2016_2009.route('/download_text4')
def download_text4():
    text_to_download = Text4.query.first()
    if text_to_download:
        # Construct the absolute path to the downloaded file
        file_path = os.path.join(app.root_path, 'downloaded_text4.txt')

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


@twi_2016_2009.route('/success/twi_2016_2009', methods=['GET'])
def download_after_payment():
    reference_id = request.args.get('reference')

    if is_valid_reference(reference_id):
        # Retrieve the text content from the database
        text_to_download = Text4.query.first()

        if text_to_download:
            # Construct the absolute path to the downloaded file
            file_path = os.path.join(app.root_path, 'downloaded_text4.txt')

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
        return redirect('https://paystack.com/pay/twi_2016_2009')
