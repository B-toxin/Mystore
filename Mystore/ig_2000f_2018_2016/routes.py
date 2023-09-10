from flask import Flask, flash, Blueprint, send_file, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from Mystore import db
import os


app = Flask(__name__)
# Define a blueprint for ran_fb-related routes
ig_2000f_2018_2016 = Blueprint('ig_2000f_2018_2016', __name__)


# Define the Text model
class Text7(db.Model):
    __bind_key__ = 'ig_2000f_2018_2016'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class AddTextForm7(FlaskForm):
    text_content7 = TextAreaField('Text Content', validators=[DataRequired()])


@ig_2000f_2018_2016.route('/ig_2000f_2018_2016_db')
def index7():
    form = AddTextForm7()
    texts = Text7.query.all()
    return render_template('database/ig_2000f_2018_2016_db.html', texts=texts, form=form)


@ig_2000f_2018_2016.route('/add_text7', methods=['POST'])
def add_text7():
    form = AddTextForm7()
    if form.validate_on_submit():
        text_content7 = form.text_content7.data  # Use 'data' instead of 'content'
        if text_content7:
            new_text = Text7(content=text_content7)  # Use 'content' instead of 'data'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/ig_2000f_2018_2016_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/ig_2000f_2018_2016_db')


@ig_2000f_2018_2016.route('/download_text7')
def download_text7():
    text_to_download = Text7.query.first()
    if text_to_download:
        # Construct the absolute path to the downloaded file
        file_path = os.path.join(app.root_path, 'downloaded_text7.txt')

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


@ig_2000f_2018_2016.route('/success/ig_2000f_2018_2016', methods=['GET'])
def download_after_payment():
    reference_id = request.args.get('reference')

    if is_valid_reference(reference_id):
        # Retrieve the text content from the database
        text_to_download = Text7.query.first()

        if text_to_download:
            # Construct the absolute path to the downloaded file
            file_path = os.path.join(app.root_path, 'downloaded_text7.txt')

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
        return redirect('https://paystack.com/pay/ig_2000f_2018_2016')
