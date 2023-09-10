from flask import Flask, flash, Blueprint, send_file,session, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from Mystore import db
import os

app = Flask(__name__)

usa_fb = Blueprint('usa_fb', __name__)


class Text1(db.Model):
    __bind_key__ = 'usa_fb'  # Use the 'new_database' configuration
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(255), nullable=False)


class AddTextForm1(FlaskForm):
    text_content1 = TextAreaField('Text Content', validators=[DataRequired()])


@usa_fb.route('/usa_fb_db')
def index1():
    form = AddTextForm1()
    texts = Text1.query.all()
    return render_template('database/usa_fb_db.html', texts=texts, form=form)


@usa_fb.route('/add_text1', methods=['POST'])
def add_text1():
    form = AddTextForm1()
    if form.validate_on_submit():
        text_content1 = form.text_content1.data
        if text_content1:
            new_text = Text1(data=text_content1)  # Use 'data' instead of 'content'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/usa_fb_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/usa_fb_db')


@usa_fb.route('/download_text1')
def download_text1():
    text_to_download = Text1.query.first()
    if text_to_download:
        # Construct the absolute path to the downloaded file
        file_path = os.path.join(app.root_path, 'downloaded_text1.txt')

        # Create a TXT file and provide it for download
        with open(file_path, 'w') as txt_file:
            txt_file.write(text_to_download.data)  # Use 'data' instead of 'content'

        # Delete the downloaded text from the database
        db.session.delete(text_to_download)
        db.session.commit()

        return send_file(file_path, as_attachment=True)
    else:
        return "No more texts to download."


# Function to check if the reference ID is valid (e.g., in a database)
def is_valid_reference(reference_id):
    return reference_id is not None


@usa_fb.route('/success/usa_fb', methods=['GET'])
def download_after_payment():
    reference_id = request.args.get('reference')

    if is_valid_reference(reference_id):
        # Retrieve the text content from the database
        text_to_download = Text1.query.first()

        if text_to_download:
            # Construct the absolute path to the downloaded file
            file_path = os.path.join(app.root_path, 'downloaded_text1.txt')

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
        return redirect('https://paystack.com/pay/usa_fb')
