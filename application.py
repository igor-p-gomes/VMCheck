from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)

vmcorreto = ""
vmchecado = ""
resultado = ""


@app.route('/')
def show_index():
    full_filename = "/static/MC_03_2_jpg.jpg"
    return render_template("index.html", user_image = full_filename)
	
@app.route('/secret')
def show_secret():
    full_filename = "MC_03_2_jpg.jpg"
    return render_template("index.html", user_image = full_filename)