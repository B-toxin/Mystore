from flask import Flask, flash, Blueprint, send_file, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from Mystore import db
import os


app = Flask(__name__)
# Define a blueprint for ran_fb-related routes
tik_1000 = Blueprint('tik_1000', __name__)


# Define the Text model
class Text2(db.Model):
    __bind_key__ = 'tik_1000'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class AddTextForm2(FlaskForm):
    text_content2 = TextAreaField('Text Content', validators=[DataRequired()])


@tik_1000.route('/tik_1000_db')
def index2():
    form = AddTextForm2()
    texts = Text2.query.all()
    return render_template('database/tik_1000_db.html', texts=texts, form=form)


@tik_1000.route('/add_text2', methods=['POST'])
def add_text2():
    form = AddTextForm2()
    if form.validate_on_submit():
        text_content2 = form.text_content2.data  # Use 'data' instead of 'content'
        if text_content2:
            new_text = Text2(content=text_content2)  # Use 'content' instead of 'data'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/tik_1000_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/tik_1000_db')


@tik_1000.route('/download_text2')
def download_text2():
    text_to_download = Text2.query.first()
    if text_to_download:
        # Construct the absolute path to the downloaded file
        file_path = os.path.join(app.root_path, 'downloaded_text2.txt')

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


@tik_1000.route('/success/tik_1000', methods=['GET', 'POST'])
def rn_fb():
    reference_id = request.args.get('reference')
    if is_valid_reference(reference_id):
        form = AddTextForm2()  # Create an instance of your form
        return render_template('downloads/download_tik_1000.html', form=form)
    else:
        return redirect('https://paystack.com/pay/tik_1000')
