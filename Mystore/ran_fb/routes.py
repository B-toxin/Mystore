from flask import Flask, flash, Blueprint, send_file, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from Mystore import db
import os


app = Flask(__name__)
# Define a blueprint for ran_fb-related routes
ran_fb = Blueprint('ran_fb', __name__)


# Define the Text model
class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class AddTextForm(FlaskForm):
    text_content = TextAreaField('Text Content', validators=[DataRequired()])


@ran_fb.route('/ran_fb_db')
def index():
    form = AddTextForm()
    texts = Text.query.all()
    return render_template('database/ran_fb_db.html', texts=texts, form=form)


@ran_fb.route('/add_text', methods=['POST'])
def add_text():
    form = AddTextForm()
    if form.validate_on_submit():
        text_content = form.text_content.data  # Use 'data' instead of 'content'
        if text_content:
            new_text = Text(content=text_content)  # Use 'content' instead of 'data'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/ran_fb_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/ran_fb_db')


@ran_fb.route('/download_text')
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


@ran_fb.route('/success/ran_fb', methods=['GET'])
def download_after_payment():
    reference_id = request.args.get('reference')

    if is_valid_reference(reference_id):
        # Retrieve the text content from the database
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

            # Send the file for download
            return send_file(file_path, as_attachment=True)
        else:
            return "No more texts to download."
    else:
        return redirect('https://paystack.com/pay/ran_fb')
