import os
from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
from flask_wtf import CSRFProtect
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e71121f8359c7c241f56e489f91f32d7'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
csrf = CSRFProtect(app)

payment = Blueprint('payment', __name__)

# Directory where files are stored
FILES_FOLDER = os.path.abspath('static/files')


def is_valid_reference(reference_id):
    return reference_id is not None


@payment.route('/success/ran_fb')
def ran_fb():
    reference_id = request.args.get('reference')
    # Check if the reference ID is valid (e.g., in a database)
    if is_valid_reference(reference_id):
        return render_template('success/success_ran_fb.html')
    else:
        # Redirect or display an error message for invalid reference IDs
        return redirect('https://paystack.com/pay/ran_fb')


@payment.route('/success/r_fb', methods=['GET', 'POST'])
def r_fb():
    if request.method == 'POST':
        # Handle the file download when the "Download" button is clicked
        # (This part of the code remains the same)
        available_files = get_available_files()
        if available_files:
            # Get the first available file
            file_to_download = available_files[0]
            file_path = os.path.join(FILES_FOLDER, file_to_download)

            # Remove the file from the list of available files
            available_files.pop(0)

            # Delete the file from the server
            os.remove(file_path)

        # After handling the download, you can redirect to the home page
        return redirect(url_for('home'))

    # The rest of your code (GET request handling) remains the same
    available_files = get_available_files()

    if available_files:
        # Generate the URL for the current file using url_for
        current_file_url = url_for('static', filename=f'files/{available_files[0]}')

        # Generate URLs for all files and pass them to the template
        file_urls = [url_for('static', filename=f'files/{file_name}') for file_name in available_files]

        return render_template('download_ran_fb.html', current_file_url=current_file_url, file_urls=file_urls)
    else:
        # Redirect to the home page or any other desired page when all files are downloaded
        return redirect(url_for('home'))


def get_available_files():
    # List files in the "files" folder that have not been downloaded yet
    downloaded_files = session.get('downloaded_files', [])
    all_files = os.listdir(FILES_FOLDER)
    available_files = [file for file in all_files if file not in downloaded_files]
    return available_files


@payment.route('/success/usa_fb')
def usa_fb():
    return None
