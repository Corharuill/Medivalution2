from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from Medievalution import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

from Medievalution import login


class User( UserMixin, db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    username= db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    password_hash= db.Column(db.String(256))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
  return db.session.get(User, int(id))

class Chat(db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    username= db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    subject = db.Column(db.String(120), index=True, unique=True)
    message = db.Column(db.Text(2000), index=True, unique=True)
    def __repr__(self):
        return '<Chat {}>'.format(self.username)