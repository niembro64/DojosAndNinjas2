from flask_app import app
from flask import render_template, request, redirect

# import the class from user.py
from flask_app.models.dojo import Dojo

@app.route("/")
def show_index():
    # call the get all classmethod to get all users
    return render_template("index.html")

@app.route("/dojos")
def show_dojos():
    # call the get all classmethod to get all users
    return render_template("dojos.html")