from flask import Flask, flash, Blueprint, send_file, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from Mystore import db
import os


app = Flask(__name__)
# Define a blueprint for ran_fb-related routes
snap_100k = Blueprint('snap_100k', __name__)


# Define the Text model
class Text10(db.Model):
    __bind_key__ = 'snap_100k'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class AddTextForm10(FlaskForm):
    text_content10 = TextAreaField('Text Content', validators=[DataRequired()])


@snap_100k.route('/snap_100k_db')
def index10():
    form = AddTextForm10()
    texts = Text10.query.all()
    return render_template('database/snap_100k_db.html', texts=texts, form=form)


@snap_100k.route('/add_text10', methods=['POST'])
def add_text10():
    form = AddTextForm10()
    if form.validate_on_submit():
        text_content10 = form.text_content10.data  # Use 'data' instead of 'content'
        if text_content10:
            new_text = Text10(content=text_content10)  # Use 'content' instead of 'data'
            db.session.add(new_text)
            db.session.commit()
            return redirect('/snap_100k_db')
        else:
            flash('Text content cannot be empty.', 'warning')
    else:
        flash('Invalid form submission. Please check your input.', 'danger')

    # If form validation fails, return to the index page with error messages
    return redirect('/snap_100k_db')


@snap_100k.route('/download_text10')
def download_text10():
    text_to_download = Text10.query.first()
    if text_to_download:
        # Construct the absolute path to the downloaded file
        file_path = os.path.join(app.root_path, 'downloaded_text10.txt')

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


@snap_100k.route('/success/snap_100k', methods=['GET', 'POST'])
def ig():
    reference_id = request.args.get('reference')
    if is_valid_reference(reference_id):
        form = AddTextForm10()  # Create an instance of your form
        return render_template('downloads/download_snap_100k.html', form=form)
    else:
        return redirect('https://paystack.com/pay/snap_100k')
