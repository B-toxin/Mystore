from flask import Flask, flash, Blueprint, send_file, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from Mystore import db
import os


app = Flask(__name__)
# Define a blueprint for ran_fb-related routes
reddit_1000k = Blueprint('reddit_1000k', __name__)


# Define the Text model
class Text13(db.Model):
    __bind_key__ = 'reddit_1000k'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class AddTextForm13(FlaskForm):
    text_content13 = TextAreaField('Text Content', validators=[DataRequired()])


@reddit_1000k.route('/reddit_1000k_db')
def index13():
    form = AddTextForm13()
    texts = Text13.query.all()
    return render_template('database/reddit_1000k_db.html', texts=texts, form=form)


@reddit_1000k.route('/add_text13', methods=['POST'])
def add_text13():
    form = AddTextForm13()
    if form.validate_on_submit():
        text_content13 = form.text_content13.data  # Use 'data' instead of 'content'
        if text_content13:
            new_text = Text13(content=text_content13)  # Use 'content' instead of 'data'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/reddit_1000k_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/reddit_1000k_db')


@reddit_1000k.route('/download_text13')
def download_text13():
    text_to_download = Text13.query.first()
    if text_to_download:
        # Construct the absolute path to the downloaded file
        file_path = os.path.join(app.root_path, 'downloaded_text13.txt')

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


@reddit_1000k.route('/success/reddit_1000k', methods=['GET'])
def download_after_payment():
    reference_id = request.args.get('reference')

    if is_valid_reference(reference_id):
        # Retrieve the text content from the database
        text_to_download = Text13.query.first()

        if text_to_download:
            # Construct the absolute path to the downloaded file
            file_path = os.path.join(app.root_path, 'downloaded_text13.txt')

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
        return redirect('https://paystack.com/pay/reddit_1000k')
