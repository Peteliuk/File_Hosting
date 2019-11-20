#import app
from filehostingapp import app

#import 'user_module' functions
from filehostingapp.user_module import UserModule
from filehostingapp.file_module import FileModule

#import flask functions
from flask import render_template
from flask import session

um = UserModule()
fm = FileModule()

@app.route('/')
def index():
	return render_template('index.html', user = session["user"] 
		if "user" in session 
		else session["login"] if "login" in session 
		else "None")

@app.route('/login', methods = ['POST', 'GET'])
def login():
	return um.login()

@app.route('/registration', methods = ['POST', 'GET'])
def registration():
	return um.registration()

@app.route('/personal?<user>', methods = ['POST', 'GET'])
def personal(user):
	return fm.personal(user)

@app.route('/settings?<user>', methods = ['POST', 'GET'])
def settings(user):
	return um.settings(user)

@app.route('/logout')
def logout():
	return um.logout()

@app.route('/delete?<filename>?<login>')
def delete(filename, login):
	return fm.delete(filename, login)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
	return fm.download(filename)