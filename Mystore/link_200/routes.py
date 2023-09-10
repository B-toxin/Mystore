from flask import Flask, flash, Blueprint, send_file, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from Mystore import db
import os


app = Flask(__name__)
# Define a blueprint for ran_fb-related routes
link_200 = Blueprint('link_200', __name__)


# Define the Text model
class Text15(db.Model):
    __bind_key__ = 'link_200'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class AddTextForm15(FlaskForm):
    text_content15 = TextAreaField('Text Content', validators=[DataRequired()])


@link_200.route('/link_200_db')
def index15():
    form = AddTextForm15()
    texts = Text15.query.all()
    return render_template('database/link_200_db.html', texts=texts, form=form)


@link_200.route('/add_text15', methods=['POST'])
def add_text15():
    form = AddTextForm15()
    if form.validate_on_submit():
        text_content15 = form.text_content15.data  # Use 'data' instead of 'content'
        if text_content15:
            new_text = Text15(content=text_content15)  # Use 'content' instead of 'data'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/link_200_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/link_200_db')


@link_200.route('/download_text15')
def download_text15():
    text_to_download = Text15.query.first()
    if text_to_download:
        # Construct the absolute path to the downloaded file
        file_path = os.path.join(app.root_path, 'downloaded_text15.txt')

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


@link_200.route('/success/link_200', methods=['GET', 'POST'])
def aged():
    reference_id = request.args.get('reference')
    if is_valid_reference(reference_id):
        form = AddTextForm15()  # Create an instance of your form
        return render_template('downloads/download_link_200.html', form=form)
    else:
        return redirect('https://paystack.com/pay/link_200')