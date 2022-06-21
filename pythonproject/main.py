#!/usr/bin/python3
from flask import Flask, request, render_template
import dbconnection as coredb
import attributes as attr

app = Flask(__name__)


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == "POST":
        email = request.form.get('email')
        name = request.form.get('name')
        surname = request.form.get('surname')
        check_mail = coredb.match_email(str(email))

        if check_mail == None:
            coredb.register_user(email, name, surname)
            return render_template('reg-success.html')
        else:
            return render_template('reg-index-fail.html')
    return render_template('reg-index.html')


@app.route("/")
def users_list():
    users = coredb.read_users()
    attr.users_on_html(users)
    return render_template("users.html")
