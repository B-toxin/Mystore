from flask import Blueprint, Flask, render_template, send_file
import sqlite3
import os

app = Flask(__name__)

pages = Blueprint('pages', __name__)


@pages.route('/')
@pages.route('/home')
def home():
    return render_template('home.html')


@pages.route('/collections/all')
def menu():
    return render_template('menu.html')


@pages.route('/pages/contact')
def contact():
    return render_template('contact.html')


@pages.route('/collections/frontpage')
def facebook():
    return render_template('countries_facebook.html')


@pages.route('/collections/instagram-account')
def instagram():
    return render_template('instagram_account.html')


@pages.route('/download/<file_identifier>')
def download_file(file_identifier):
    conn = sqlite3.connect('file_data.db')
    c = conn.cursor()

    # Query the database for the file by file_identifier
    c.execute('SELECT filename FROM files WHERE filename LIKE ?', (f'%{file_identifier}%',))
    result = c.fetchone()

    if result:
        filename = result[0]
        file_path = os.path.join('static/files', filename)
        conn.close()

        # Send the file for download
        return send_file(file_path, as_attachment=True)

    conn.close()
    return 'File not found'
