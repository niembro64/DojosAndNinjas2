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
    dojos = Dojo.all_dojos()
    return render_template("dojos.html", all_dojos = dojos)

###################

@app.route("/fun_create_dojo", methods=["POST"])
def fun_create_dojo():
    data = {
        "name": request.form["name"]
    }
    dojo_id = Dojo.save_dojo(data)
    return redirect("/dojos")