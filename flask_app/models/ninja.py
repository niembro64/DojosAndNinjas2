from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import dojo

class Ninja:
    def __init__(self, data):
        self.id = data["id"]

        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
            
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.dojo_id = data["dojo_id"]

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"
        new_id = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return new_id

    # @classmethod
    # def get_ninjas_in_dojos(cls):
    #     query = "SELECT * FROM ninjas JOIN dojos on dojos.id = ninjas.dojo_id;"
    #     results = connectToMySQL("dojos_and_ninjas").query_db(query)
    #     all_ninjas_w_dojos = []
    #     for row in results:
    #          one_ninja = cls(row)
    #          dojo_data = {
    #              "id" : row["dojos.id"],
    #              "name" : row["name"],
    #              "created_at" : row["dojos.created_at"],
    #              "updated_at" : row["dojos.updated_at"]
    #          }
    #          one_ninja.dojo = dojo.Dojo(dojo_data)
    #          all_ninjas_w_dojos.append(one_ninja)
    #     return all_ninjas_w_dojos

    @classmethod
    def get_ninjas_in_a_dojo(cls, data):
        query = "SELECT * FROM ninjas JOIN dojos on dojos.id = ninjas.dojo_id WHERE ninjas.dojo_id = %(dojo_id)s;"
        # query = "INSERT INTO ninjas (created_at, updated_at, dojo_id) VALUES (NOW(), NOW(), %(id)s);"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        all_ninjas_w_dojos = []
        for row in results:
             one_ninja = cls(row)
             dojo_data = {
                 "id" : row["dojos.id"],
                 "name" : row["name"],
                 "created_at" : row["dojos.created_at"],
                 "updated_at" : row["dojos.updated_at"]
             }
             one_ninja.dojo = dojo.Dojo(dojo_data)

             all_ninjas_w_dojos.append(one_ninja)
        return all_ninjas_w_dojos
