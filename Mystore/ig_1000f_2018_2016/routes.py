from flask import Flask, flash, Blueprint, send_file, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from Mystore import db
import os


app = Flask(__name__)
# Define a blueprint for ran_fb-related routes
ig_1000f_2018_2016 = Blueprint('ig_1000f_2018_2016', __name__)


# Define the Text model
class Text8(db.Model):
    __bind_key__ = 'ig_1000f_2018_2016'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class AddTextForm8(FlaskForm):
    text_content8 = TextAreaField('Text Content', validators=[DataRequired()])


@ig_1000f_2018_2016.route('/ig_1000f_2018_2016_db')
def index8():
    form = AddTextForm8()
    texts = Text8.query.all()
    return render_template('database/ig_1000f_2018_2016_db.html', texts=texts, form=form)


@ig_1000f_2018_2016.route('/add_text8', methods=['POST'])
def add_text8():
    form = AddTextForm8()
    if form.validate_on_submit():
        text_content8 = form.text_content8.data  # Use 'data' instead of 'content'
        if text_content8:
            new_text = Text8(content=text_content8)  # Use 'content' instead of 'data'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/ig_1000f_2018_2016_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/ig_1000f_2018_2016_db')


@ig_1000f_2018_2016.route('/download_text8')
def download_text8():
    text_to_download = Text8.query.first()
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


@ig_1000f_2018_2016.route('/success/ig_1000f_2018_2016', methods=['GET', 'POST'])
def ig():
    reference_id = request.args.get('reference')
    if is_valid_reference(reference_id):
        form = AddTextForm8()  # Create an instance of your form
        return render_template('downloads/download_ig_1000f_2018_2016.html', form=form)
    else:
        return redirect('https://paystack.com/pay/ig_1000f_2018_2016')
