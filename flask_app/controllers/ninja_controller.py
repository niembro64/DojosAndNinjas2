from flask_app import app
from flask import render_template, request, redirect

# import the class from user.py
from flask_app.models.ninja import Ninja

@app.route("/")
def index():
    # call the get all classmethod to get all users
    return render_template("index.html")