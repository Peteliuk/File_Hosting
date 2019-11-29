import os
from flask import Flask
from filehostingapp.file_functions import basedir

app = Flask(__name__)
app.secret_key = "sk"
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, "uploads")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + \
    os.path.join(basedir, "database.db")

from filehostingapp import routes