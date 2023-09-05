from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
from flask_wtf import CSRFProtect
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e71121f8359c7c241f56e489f91f32d7'
app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem-based session storage
Session(app)
csrf = CSRFProtect(app)

payment = Blueprint('payment', __name__)


def is_valid_reference(reference_id):
    return reference_id is not None


# Function to check if the user has already downloaded the content
def has_downloaded():
    return session.get('downloaded', False)


@payment.route('/success/ran_fb')
def ran_fb():
    reference_id = request.args.get('reference')
    # Check if the reference ID is valid (e.g., in a database)
    if is_valid_reference(reference_id):
        return render_template('success/success_ran_fb.html')
    else:
        # Redirect or display an error message for invalid reference IDs
        return redirect('https://paystack.com/pay/ran_fb')


def get_available_files():
    # List of file names in the "files" folder
    file_names = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']  # Add your file names here

    # Retrieve the downloaded files from the session, default to an empty list
    downloaded_files = session.get('downloaded_files', [])

    # Remove downloaded files from the available files list
    available_files = [file for file in file_names if file not in downloaded_files]

    return available_files


@payment.route('/success/r_fb', methods=['GET', 'POST'])
def r_fb():
    # Retrieve the current file index from the session
    file_index = session.get('file_index', 0)

    if request.method == 'POST':
        # Increment the file index after a download
        file_index += 1
        session['file_index'] = file_index

        # Record the downloaded file and update the session
        downloaded_files = session.get('downloaded_files', [])
        available_files = get_available_files()

        if file_index <= len(available_files):
            downloaded_file = available_files[file_index - 1]
            downloaded_files.append(downloaded_file)
            session['downloaded_files'] = downloaded_files

    available_files = get_available_files()

    if file_index < len(available_files):
        # Generate the URL for the current file using url_for
        current_file_url = url_for('static', filename=f'files/{available_files[file_index]}')

        # Generate URLs for all files and pass them to the template
        file_urls = [url_for('static', filename=f'files/{file_name}') for file_name in available_files]

        return render_template('download_ran_fb.html', current_file_url=current_file_url, file_urls=file_urls)
    else:
        # Reset the file index if all files have been downloaded
        session.pop('file_index', None)

        # Redirect to the home page or any other desired page
        return redirect(url_for('home'))


@payment.route('/success/usa_fb')
def usa_fb():
    # Check if the user has already downloaded the content
    if has_downloaded():
        # Redirect them to the home page or display an error message
        return render_template('home.html')

    reference_id = request.args.get('reference')

    # Check if the reference ID is valid (e.g., in a database)
    if is_valid_reference(reference_id):
        session['downloaded'] = True  # Set the download flag
        return render_template('success/success_usa_fb.html')
    else:
        # Redirect or display an error message for invalid reference IDs
        return redirect('https://paystack.com/pay/usa_fb')
