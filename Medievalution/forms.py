from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, Form
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  username = StringField('Username', [validators.Length(min=4, max=25)])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')
