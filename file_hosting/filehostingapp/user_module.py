# import flask functions
from flask import url_for
from flask import request
from flask import redirect
from flask import flash
from flask import session
from flask import send_from_directory
from flask import render_template

#import app
from filehostingapp import app

# import database functions
from filehostingapp.db_functions import get_user_id
from filehostingapp.db_functions import select_user
from filehostingapp.db_functions import insert_user
from filehostingapp.db_functions import update_user
from filehostingapp.db_functions import check_user

# import file functions
from filehostingapp.file_functions import regex_validation
from filehostingapp.file_functions import size_validation


class UserModule:
    def login(self):
        # When you are logged then pressed "Back", you will be redirected to
        # home
        if "user" in session or "login" in session:
            return redirect(url_for('index'))
        if request.method == 'POST':
            login = request.form['login']
            password = request.form['password']
            if regex_validation(login) and regex_validation(password):
                user = select_user(login, password)
                if user:
                    session["login"] = login
                    if user.name:
                        session["user"] = f"{user.name} {user.surname}"
                    return redirect(url_for('personal', user=session["user"]
                                            if "user" in session
                                            else session["login"] if "login" in session
                                            else None))
                else:
                    flash("This account is none! Please check your login or password!")
                    return redirect(url_for('login'))
            else:
                flash("You turned off the front-end validation. I'll tell your ma!")
                return redirect(url_for('logout'))
        return render_template('login.html')

    def registration(self):
        # When you are registered then pressed "Back", you will be redirected
        # to home
        if "user" in session or "login" in session:
            return redirect(url_for('index'))
        if request.method == 'POST':
            login = request.form['login']
            password = request.form['password']
            if size_validation(login, 30) and size_validation(password, 30):
                if regex_validation(login) and regex_validation(password):
                    if check_user(get_user_id(login)):
                        flash("This login is exist!")
                        return redirect(url_for('registration'))
                    else:
                        session["login"] = login
                        insert_user(login, password)
                        return redirect(
                            url_for(
                                'personal',
                                user=session["login"]))
                else:
                    flash("You turned off the front-end validation. I'll tell your ma!")
                    return redirect(url_for('logout'))
            else:
                flash("Min text size is 3, max is 30")
                return redirect(url_for('registration'))
        return render_template('registration.html')

    def settings(self, user):
        if request.method == 'POST':
            user_name = request.form['name']
            user_surname = request.form['surname']
            if size_validation(
                    user_name,
                    40) and size_validation(
                    user_surname,
                    50):
                if regex_validation(
                        user_name) and regex_validation(user_surname):
                    update_user(
                        get_user_id(
                            session["login"]),
                        user_name,
                        user_surname)
                    session["user"] = f"{user_name} {user_surname}"
                    return redirect(url_for('personal', user=session["user"]))
                else:
                    flash("You turned off the front-end validation. I'll tell your ma!")
                    return redirect(url_for('logout'))
            else:
                flash(
                    "Min text size is 3, max is 40 for user name and 50 for user surname")
                return redirect(url_for('settings', user=user))
        return render_template('settings.html', user=user)

    def logout(self):
        session.pop("user", None)
        session.pop("login", None)
        return redirect(url_for('index'))
