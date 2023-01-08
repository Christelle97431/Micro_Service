#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, flash, session, url_for, get_flashed_messages,jsonify
from model import UserModel
import hashlib #pour le hash du password
import re #pour les regex


def flash_message(message, category):
    flash(message, category)
    print(f'la category {category}')
    return category


def index():
    # users = get_users()
    # return render_template('index.html', users=users)
    return render_template('index.html')


def check_email(email):
    # try:
    #     parsed_email = parse_email_address(email)
    #     return parsed_email.address == email
    # except ValueError:

    #     return False
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.fullmatch(regex, email) is not None


def CreateController(mysql):
    print("dans le register")
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    password_confirm = request.form['password_confirmation']
    print(f"Hello {username}")
    if request:
        if check_email(email):
            if password_confirm == password:
                hash_object = hashlib.sha256(password.encode())
                password_hash = hash_object.hexdigest()
                UserModel.create_user(mysql, username, email, password_hash)
                return 1
            else:
                return 0
        else:
            return 2


def LoginController(mysql):
    email = request.form['email']
    password = request.form['password']
    hash_object = hashlib.sha256(password.encode())
    password_hash_login = hash_object.hexdigest()
    # print(f"password saisi lors du login et hashé : {password_hash_login}")
    myresult = UserModel.login_user(mysql, email)
    # print(f"résultat BDD : {myresult}")
    if len(myresult) == 0:
        return -1
    else:
        for elem in myresult:
            # print(elem)
            # print(f"id : {elem[3]}")
            if elem[3] == password_hash_login:
                return 1
            else:
                return 0


def ShowController(mysql, user_id):
    result = UserModel.show_user(mysql, user_id)
    return(result)


def ShowAllController(mysql):
    result = UserModel.get_users(mysql)
    return(result)

  
def UpdateController(mysql, request):
    email = request['email']
    username = request['username']
    id = request['id']
    password = request['password']
    hash_object = hashlib.sha256(password.encode())
    password_hash = hash_object.hexdigest()
    result = UserModel.edit_user(mysql, email, username, password_hash, id)
    return(result)


def DeleteController(mysql, user_id):
    result = UserModel.destroy_user(mysql, user_id)
    return(result)
