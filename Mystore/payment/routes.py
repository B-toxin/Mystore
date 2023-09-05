from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e71121f8359c7c241f56e489f91f32d7'
csrf = CSRFProtect(app)

payment = Blueprint('payment', __name__)


def is_valid_reference(reference_id):
    return reference_id is not None


@payment.route('/success/usa_fb')
def usa_fb():
    # Check if the user has already downloaded the content
    if session.get('downloaded'):
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
    # List of file names in the "files" folder
    file_names = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']  # Add your file names here

    # Retrieve the current file index from the session
    file_index = session.get('file_index', 0)

    if request.method == 'POST':
        # Increment the file index after a download
        file_index += 1
        session['file_index'] = file_index

    if file_index < len(file_names):
        # Generate the URL for the current file using url_for
        current_file_url = url_for('static', filename=f'files/{file_names[file_index]}')

        # Generate URLs for all files and pass them to the template
        file_urls = [url_for('static', filename=f'files/{file_name}') for file_name in file_names]

        return render_template('download_ran_fb.html', current_file_url=current_file_url, file_urls=file_urls)
    else:
        # Reset the file index if all files have been downloaded
        session.pop('file_index', None)

        # Redirect to the home page or any other desired page
        return redirect(url_for('home'))
