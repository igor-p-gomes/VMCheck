from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def show_index():
    full_filename = 'MC_03_2_jpg.jpg'
    return render_template("/index.html", user_image = full_filename)