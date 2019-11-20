import sqlite3
import os
from filehostingapp.file_functions import basedir
from filehostingapp import app

# SQL Queries
# Connect to database
with sqlite3.connect(f'{basedir}/data.db', check_same_thread = False) as mydb:
	# Get user's id
	def get_user_id(login):
		sql = f"SELECT users.id FROM users WHERE users.login = '{login}'"
		cur = mydb.cursor()
		cur.execute(sql)
		result = cur.fetchall()
		return result[0][0] if result else -1

	# Select all from 'user_files' table
	def select_files(user_id):
		sql = f"SELECT * FROM user_files WHERE user_id = {user_id}"
		cur = mydb.cursor()
		cur.execute(sql)
		result = cur.fetchall()
		data = [] # List for filename and filepath
		for res in result:
			# Append to 'data' list touple(s) within filename and filepath
			data.append((res[0],res[1]))
		return data

	# Insert values to 'user_files' table
	def insert_file(*args):
		sql = "INSERT INTO user_files VALUES (?,?,?)"
		cur = mydb.cursor()
		cur.execute(sql,args)
		mydb.commit()

	# Delete row from 'user_files' table
	def delete_file(*args):
		sql = f"""DELETE FROM user_files 
		WHERE user_files.filename = '{args[0]}'
		AND user_files.user_id = {args[1]}"""
		cur = mydb.cursor()
		cur.execute(sql)
		mydb.commit()
		os.remove(os.path.join(app.config['UPLOAD_FOLDER'], args[0]))

	# Insert login and password to 'users' table
	def insert_data(*args):
		sql = "INSERT INTO users (login, password) VALUES (?,?)"
		cur = mydb.cursor()
		cur.execute(sql,args)
		mydb.commit()

	# Select all data from 'users' table
	def select_data(user_id):
		sql = f"SELECT * FROM users WHERE users.id = {user_id}"
		cur = mydb.cursor()
		cur.execute(sql)
		return cur.fetchall()

	# Check if login exists
	def check_data(login):
		cur = mydb.cursor()
		cur.execute("SELECT login FROM users")
		res = cur.fetchall()
		for r in res:
			if login == r[0]:
				return "exist"
				break

	# Update 'users' table: set user's name and surname
	def update_data(*args):
		sql = f"""
		UPDATE users 
		SET name = '{args[0]}', surname = '{args[1]}' 
		WHERE id = {args[2]}
		"""
		cur = mydb.cursor()
		cur.execute(sql)
		mydb.commit()