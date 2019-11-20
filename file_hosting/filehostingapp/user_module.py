#import app
from filehostingapp import app

#import flask functions
from flask import url_for
from flask import request
from flask import redirect
from flask import flash
from flask import session
from flask import send_from_directory
from flask import render_template

#import database functions
from filehostingapp.db_functions import get_user_id
from filehostingapp.db_functions import select_data
from filehostingapp.db_functions import insert_data
from filehostingapp.db_functions import update_data
from filehostingapp.db_functions import check_data

class UserModule:
	def login(sel):
		if "user" in session or "login" in session:
			return redirect(url_for('index'))
		if request.method == 'POST':
			login = request.form['login']
			password = request.form['password']
			res = select_data(get_user_id(login))
			if res:
				session["login"] = login
				if res[0][3]:
					session["user"] = f"{res[0][3]} {res[0][4]}"
				return redirect(url_for('personal', user = session["user"] 
					if "user" in session 
					else session["login"] if "login" in session 
					else "None"))
			else:
				flash("This account is none! Please check your login or password!")
				return redirect(url_for('login'))
		return render_template('login.html')

	def registration(self):
		if "user" in session or "login" in session:
			return redirect(url_for('index'))
		if request.method == 'POST':
			login = request.form['login']
			password = request.form['password']
			if check_data(login) != "exist":
				session["login"] = login
				insert_data(login,password)
				return redirect(url_for('personal', user = session["login"]))
			else:
				flash("This login is exist!")
				return redirect(url_for('registration'))
		return render_template('registration.html')

	def settings(self,user):
		if request.method == 'POST':
			user_name = request.form['name']
			user_surname = request.form['surname']
			update_data(user_name, user_surname, get_user_id(session["login"]))
			session["user"] = f"{user_name} {user_surname}"
			return redirect(url_for('personal', user = session["user"]))
		return render_template('settings.html', user = user)

	def logout(self):
		session.pop("user", None)
		session.pop("login", None)
		return redirect(url_for('index'))