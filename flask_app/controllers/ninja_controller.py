from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/new_ninja")
def new_ninja():
    a = Dojo.all_dojos()
    return render_template("new_ninja.html", all_dojos = a)

# @app.route("/dojos/0")
# def view_ninjas_in_dojos():
#     dojo_with_ninjas = Ninja.get_ninjas_in_dojos()
#     return render_template("ninjas_in_dojo.html", ninjas_in_dojos = dojo_with_ninjas)

@app.route("/dojos/<int:dojo_id>")
def view_dojo(dojo_id):
    data = {
        "dojo_id": dojo_id
    }
    dojo_with_ninjas = Ninja.get_ninjas_in_a_dojo(data)
    return render_template("ninjas_in_dojo.html", ninjas_in_a_dojo = dojo_with_ninjas)



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
