from flask import Flask, flash, Blueprint, send_file, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField, PasswordField
from wtforms.validators import DataRequired, InputRequired
from Mystore import db
import os
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
csrf = CSRFProtect(app)
correct_password = 'b8b7ce3756a3abcd'

gv_usa = Blueprint('gv_usa', __name__)


# Define the Text model
class Text16(db.Model):
    __bind_key__ = 'gv_usa'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[InputRequired()])


class AddTextForm16(FlaskForm):
    text_content16 = TextAreaField('Text Content', validators=[DataRequired()])


@gv_usa.route('/gv_usa_db', methods=['GET', 'POST'])
def index16():
    form = PasswordForm()

    if form.validate_on_submit():
        password_attempt = form.password.data

        if password_attempt == correct_password:
            # Password is correct, render the protected page
            form = AddTextForm16()
            texts = Text16.query.all()
            return render_template('database/gv_usa_db.html', texts=texts, form=form)
        else:
            # Password is incorrect, show an error message
            flash("Incorrect password. Please try again.", 'error')

    # If it's a GET request or the form is invalid, show the password prompt
    return render_template('downloads/download_gv_usa.html', form=form)


@gv_usa.route('/add_text16', methods=['POST'])
def add_text16():
    form = AddTextForm16()
    if form.validate_on_submit():
        text_content16 = form.text_content16.data  # Use 'data' instead of 'content'
        if text_content16:
            new_text = Text16(content=text_content16)  # Use 'content' instead of 'data'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/gv_usa_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/gv_usa_db')


@gv_usa.route('/download_text16')
def download_text16():
    text_to_download = Text16.query.first()
    if text_to_download:
        # Construct the absolute path to the downloaded file
        file_path = os.path.join(app.root_path, 'downloaded_text16.txt')

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
    return reference_id is None


@gv_usa.route('/success/gv_usa', methods=['GET'])
def download_after_payment():
    reference_id = request.args.get('reference')

    if is_valid_reference(reference_id):
        # Retrieve the text content from the database
        text_to_download = Text16.query.first()

        if text_to_download:
            # Construct the absolute path to the downloaded file
            file_path = os.path.join(app.root_path, 'downloaded_text16.txt')

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
        return redirect('https://flutterwave.com/pay/gv_usa')
