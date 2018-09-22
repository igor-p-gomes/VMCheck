import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from azure.storage.blob import BlockBlobService
import string, random, requests
from flask.ext.azure_storage import FlaskAzureStorage

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
AZURE_STORAGE_ACCOUNT_NAME = "your-account-name"
AZURE_STORAGE_ACCOUNT_KEY = "your-account-key"


app = Flask(__name__)
azure_storage = FlaskAzureStorage(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template("index.html", user_image = full_filename)