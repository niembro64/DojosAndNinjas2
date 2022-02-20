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


    @classmethod
    def get_ninjas_in_dojo(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = 2;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)
        all_ninjas = []
        for one_ninja in results:
            all_ninjas.append( cls(one_ninja) )
        return all_ninjas
