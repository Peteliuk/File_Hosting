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

#import file function
from filehostingapp.file_functions import change_file_name
from filehostingapp.file_functions import allowed_file

#import database functions
from filehostingapp.db_functions import get_user_id
from filehostingapp.db_functions import select_files
from filehostingapp.db_functions import delete_file
from filehostingapp.db_functions import insert_file

import os

class FileModule:
	def personal(self,user):
		if request.method == 'POST':
			file = request.files['file']
			if file and allowed_file(file.filename):
				filename = change_file_name(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			else:
				flash(f"""Allowed file formats are: 
					{list(ALLOWED_EXTENSIONS)[:]}
					""")
				return redirect(url_for('personal', user = session["user"] 
					if "user" in session 
					else session["login"] if "login" in session 
					else "None")) 
			filepath = f"{app.config['UPLOAD_FOLDER']}/{filename}"
			insert_file(filename, filepath, get_user_id(session["login"]))
			return redirect(url_for('personal', user = session["user"] 
				if "user" in session 
				else session["login"] if "login" in session 
				else "None"))
		return render_template('personal.html', user = user, data = select_files(get_user_id(session["login"])))

	def delete(self,filename,login):
		delete_file(filename,get_user_id(login))
		return redirect(url_for('personal',user = session["user"] 
			if "user" in session 
			else session["login"] if "login" in session 
			else "None"))

	def download(self,filename):
		return send_from_directory(directory=app.config["UPLOAD_FOLDER"], filename=filename)