from flask import Flask, flash, Blueprint, send_file, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from Mystore import db
import os


app = Flask(__name__)
# Define a blueprint for ran_fb-related routes
ig_f_2018_2016 = Blueprint('ig_f_2018_2016', __name__)


# Define the Text model
class Text5(db.Model):
    __bind_key__ = 'ig_f_2018_2016'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class AddTextForm5(FlaskForm):
    text_content5 = TextAreaField('Text Content', validators=[DataRequired()])


@ig_f_2018_2016.route('/ig_f_2018_2016_db')
def index5():
    form = AddTextForm5()
    texts = Text5.query.all()
    return render_template('database/ig_f_2018_2016_db.html', texts=texts, form=form)


@ig_f_2018_2016.route('/add_text5', methods=['POST'])
def add_text5():
    form = AddTextForm5()
    if form.validate_on_submit():
        text_content5 = form.text_content5.data  # Use 'data' instead of 'content'
        if text_content5:
            new_text = Text5(content=text_content5)  # Use 'content' instead of 'data'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/ig_f_2018_2016_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/ig_f_2018_2016_db')


@ig_f_2018_2016.route('/download_text5')
def download_text5():
    text_to_download = Text5.query.first()
    if text_to_download:
        # Construct the absolute path to the downloaded file
        file_path = os.path.join(app.root_path, 'downloaded_text5.txt')

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


@ig_f_2018_2016.route('/success/ig_f_2018_2016', methods=['GET'])
def download_after_payment():
    reference_id = request.args.get('reference')

    if is_valid_reference(reference_id):
        # Retrieve the text content from the database
        text_to_download = Text5.query.first()

        if text_to_download:
            # Construct the absolute path to the downloaded file
            file_path = os.path.join(app.root_path, 'downloaded_text5.txt')

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
        return redirect('https://paystack.com/pay/ig_f_2018_2016')
