import os
from filehostingapp import app
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet

key = b'JDyFtqaqzubH390IS3h3ALHpVLDJVSGvgPrkuXb86jE='
f = Fernet(key)
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    login = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(40), nullable=True)
    surname = db.Column(db.String(50), nullable=True)


class Files(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    filename = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)


def get_user_id(login):
    select = Users.query.filter_by(login=login).first()
    return select.id if select else None


def select_user(*args):
    select = Users.query.filter_by(login=args[0]).first()
    return select if select and f.decrypt(
        select.password) == args[1].encode() else None


def check_user(user_id):
    select = Users.query.filter_by(id=user_id).first()
    return select


def insert_user(*args):
    insert = Users(login=args[0], password=f.encrypt(args[1].encode()))
    db.session.add(insert)
    db.session.commit()


def update_user(*args):
    select = Users.query.filter_by(id=args[0]).first()
    select.name = args[1]
    select.surname = args[2]
    db.session.commit()


def select_files(user_id):
    select = Files.query.filter_by(user_id=user_id).all()
    return select


def insert_file(*args):
    insert = Files(user_id=args[0], filename=args[1])
    db.session.add(insert)
    db.session.commit()


def delete_file(*args):
    del_file = Files.query.filter_by(user_id=args[0], filename=args[1]).first()
    db.session.delete(del_file)
    db.session.commit()
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], args[1]))