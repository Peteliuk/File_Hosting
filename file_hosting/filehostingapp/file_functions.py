import os
import random

basedir = os.path.abspath(os.path.dirname(__file__)) # Find base folder 
UPLOAD_FOLDER = basedir + '/uploads' # Generate folder for uploads
def upload_folder():
	return UPLOAD_FOLDER
# Allowed file's formats
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'ppt', 'csv', 'xls'])
def allowed_extentions():
	return list(ALLOWED_EXTENSIONS)
# Generate new file name
def change_file_name(filename):
	arr = filename.split(".")
	return f"file{random.randint(0,10000000000)}.{arr[len(arr)-1]}"

# Generate allowed file name
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
