from flask import Flask
from filehostingapp.file_functions import upload_folder

app = Flask(__name__)
app.secret_key = "sk"
app.config['UPLOAD_FOLDER'] = upload_folder()


from filehostingapp import routes