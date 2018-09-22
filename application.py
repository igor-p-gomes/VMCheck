from flask import Flask, render_template, request, url_for
import os
from PIL import Image

app = Flask(__name__)

vmcorreto = ""
vmchecado = ""
resultado = ""


@app.route('/')
def show_index():
    full_filename = "/static/MC_03_2_jpg.jpg"
    return render_template("index.html", user_image = full_filename)
	
@app.route('/match/<fname>')
def match_fname(fname):
    full_filename = "/static/"+fname+".jpg"
	vmcorreto = open("static/"+fname+".jpg","rb").read()
    return render_template("index.html", user_image = full_filename)