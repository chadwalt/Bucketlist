
from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("login/index.html")

@app.route('/signup')
def signup():
    return render_template("login/signup.html")