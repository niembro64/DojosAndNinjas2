from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/new_ninja")
def new_ninja():
    return render_template("new_ninja.html")

@app.route("/dojos/<int:dojo_id>")
def view_dojo(dojo_id):
    data = {
        "dojo_id": dojo_id
    }
    ninjas = Ninja.get_ninjas_in_dojo(data)
    return render_template("ninjas_in_dojo.html", ninjas_in_dojo = ninjas)


###################

@app.route("/create_ninja", methods=["POST"])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    ninja_id = Ninja.save_ninja(data)
    return redirect("/dojos")
