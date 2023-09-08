from flask import Flask, flash, Blueprint, send_file, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from Mystore import db
import os


app = Flask(__name__)
# Define a blueprint for ran_fb-related routes
snap_50k = Blueprint('snap_50k', __name__)


# Define the Text model
class Text9(db.Model):
    __bind_key__ = 'snap_50k'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class AddTextForm9(FlaskForm):
    text_content9 = TextAreaField('Text Content', validators=[DataRequired()])


@snap_50k.route('/snap_50k_db')
def index9():
    form = AddTextForm9()
    texts = Text9.query.all()
    return render_template('database/snap_50k_db.html', texts=texts, form=form)


@snap_50k.route('/add_text9', methods=['POST'])
def add_text9():
    form = AddTextForm9()
    if form.validate_on_submit():
        text_content9 = form.text_content9.data  # Use 'data' instead of 'content'
        if text_content9:
            new_text = Text9(content=text_content9)  # Use 'content' instead of 'data'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/snap_50k_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/snap_50k_db')


@snap_50k.route('/download_text9')
def download_text9():
    text_to_download = Text9.query.first()
    if text_to_download:
        # Construct the absolute path to the downloaded file
        file_path = os.path.join(app.root_path, 'downloaded_text9.txt')

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


@snap_50k.route('/success/snap_50k', methods=['GET', 'POST'])
def ig():
    reference_id = request.args.get('reference')
    if is_valid_reference(reference_id):
        form = AddTextForm9()  # Create an instance of your form
        return render_template('downloads/download_snap_50k.html', form=form)
    else:
        return redirect('https://paystack.com/pay/snap_50k')
