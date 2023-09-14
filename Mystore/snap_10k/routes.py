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

snap_10k = Blueprint('snap_10k', __name__)


# Define the Text model
class Text11(db.Model):
    __bind_key__ = 'snap_10k'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[InputRequired()])


class AddTextForm11(FlaskForm):
    text_content11 = TextAreaField('Text Content', validators=[DataRequired()])


@snap_10k.route('/snap_10k_db', methods=['GET', 'POST'])
def index11():
    form = PasswordForm()

    if form.validate_on_submit():
        password_attempt = form.password.data

        if password_attempt == correct_password:
            # Password is correct, render the protected page
            form = AddTextForm11()
            texts = Text11.query.all()
            return render_template('database/snap_10k_db.html', texts=texts, form=form)
        else:
            # Password is incorrect, show an error message
            flash("Incorrect password. Please try again.", 'error')

    # If it's a GET request or the form is invalid, show the password prompt
    return render_template('downloads/download_snap_10k.html', form=form)


@snap_10k.route('/add_text11', methods=['POST'])
def add_text11():
    form = AddTextForm11()
    if form.validate_on_submit():
        text_content11 = form.text_content11.data  # Use 'data' instead of 'content'
        if text_content11:
            new_text = Text11(content=text_content11)  # Use 'content' instead of 'data'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/snap_10k_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/snap_10k_db')


@snap_10k.route('/download_text11')
def download_text11():
    text_to_download = Text11.query.first()
    if text_to_download:
        # Construct the absolute path to the downloaded file
        file_path = os.path.join(app.root_path, 'downloaded_text11.txt')

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


@snap_10k.route('/success/snap_100k', methods=['GET'])
def download_after_payment():
    reference_id = request.args.get('reference')

    if is_valid_reference(reference_id):
        # Retrieve the text content from the database
        text_to_download = Text11.query.first()

        if text_to_download:
            # Construct the absolute path to the downloaded file
            file_path = os.path.join(app.root_path, 'downloaded_text11.txt')

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
        return redirect('https://flutterwave.com/pay/snap_10k')
