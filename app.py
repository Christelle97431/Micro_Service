#!/usr/bin/env python3
from flask import Flask, render_template, request, flash, session, url_for, redirect
from flask_mysqldb import MySQL
from controller import CreateController, LoginController, ShowController, ShowAllController, DeleteController, UpdateController
import controller

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'some random string'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


def flash_message(message, category):
    flash(message, category)


@app.route('/')
def index():
    # return('bonjour')
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        x = CreateController(mysql)
        if x == 1:
            flash_message("Bravo, vous êtes enregistré(e)!", "success")
            return redirect("/")
        elif x == 0:
            flash_message("password don't match", "error")
            return redirect("/register")
        elif x == 2:
            flash_message("email invalid", "error")
            return redirect("/register")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        x = LoginController(mysql)
        if x == 0:
            flash_message(f"Sorry, wrong password !", "error")
            return redirect("/login")
        elif x == 1:
            flash_message(f"You are logged, well done !", "success")
            # return ("toto")
            return redirect("/")
        else:
            flash_message("Unknown user, please register now !", "error")
        return redirect("/register")

@app.route('/user/',methods=['GET'])
def change1():
    if request.method == 'GET':
        # id=request.args.get('id')
        print('methode GET All USERS')
        all_user = ShowAllController(mysql)
        return redirect("http://localhost:3000")


@app.route('/user', methods=['GET', 'PUT', 'DELETE', 'POST'])
def change():
    if request.method == 'POST':
        id = request.form['id']
        # print(f"id dans app : {id}")
        # print("je suis dans le Post 1 user")
        one_user = ShowController(mysql, id)
        return redirect("http://localhost:3000")
        # return (one_user)
    # elif request.method == 'GET':
    #     # id=request.args.get('id')
    #     print('methode GET All USERS')
    #     all_user = ShowAllController(mysql)
    #     return redirect("http://localhost:3000")
    elif request.method == 'DELETE':
        id = request.form['id']
        # id=request.args.get('id')
        print("id du Delete : {id}")
        delete_user = DeleteController(mysql, id)
        # return ("delete user successfull")
        return redirect("http://localhost:3000")
    elif request.method == 'PUT':
        put_user = UpdateController(mysql, request.form)
    return (put_user)

@app.route('/delete',methods=['POST'])
def delete():
    print ("dans le delete")
    if request.method == 'POST':
        id = request.form['id']
        delete_user = DeleteController(mysql, id)
        return redirect("http://localhost:3000")


# A mettre toujours à la fin
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='localhost', port=5000)
