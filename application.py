from flask import Flask, render_template, request, url_for
import os
from PIL import Image
import glob
#import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)

vmcorreto = ""
vmchecado = ""
resultado = ""

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['jpg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def show_index():
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
	
@app.route('/match/<fname>')
def match_fname(fname):
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], fname+".jpg")
	#vmcorreto = open(full_filename,"rb").read()
    return render_template("index.html", user_image = full_filename)