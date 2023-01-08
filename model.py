#!/usr/bin/env python3
from flask_mysqldb import MySQL
import hashlib
import json
from flask import jsonify


class UserModel:
    def __init__(self, username, email, password, password_confirm):
        self.username = username
        self.email = email
        self.password = password
        self.password_confirm = password_confirm
        self.ResultLoginUser = ""

    def create_user(mysql, username, email, password_hash):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users(username,email,password) VALUES(%s,%s,%s)",
                       (username, email, password_hash))
        mysql.connection.commit()
        cursor.close()


    def get_users(mysql):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users")
        users_list = cursor.fetchall()
        cursor.close()
        user_list_json = jsonify(users_list)
        with open("data.json", "w") as f:
            # Écrire le contenu de la réponse de l'application dans le fichier
            json.dump(user_list_json.json, f, indent=4)
        return user_list_json


    def login_user(mysql, email):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        Result = cursor.fetchall()
        cursor.close()
        return (Result)



    def show_user(mysql, id):
        print(f"id : {id}")
        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE id={id}")
        Result = cursor.fetchall()
        print(Result)
        result_json = jsonify(Result)
        cursor.close()
        with open("data.json", "w") as f:
            # Écrire le contenu de la réponse de l'application dans le fichier
            json.dump(result_json.json, f, indent=4)
        return (result_json)


    def destroy_user(mysql, id):
        cursor = mysql.connection.cursor()
        cursor.execute(f"DELETE FROM users WHERE id={id}")
        cursor.close()
        return jsonify('User deleted successfully !')

    def edit_user(mysql, email, username, password, id):
        cursor = mysql.connection.cursor()
        cursor.execute('''UPDATE `users` SET `username`= %s, `email`= %s, `password`= %s WHERE id=%s''',(username,email,password, id))
        mysql.connection.commit()
        cursor.close()
        return jsonify('User updated successfully !')
