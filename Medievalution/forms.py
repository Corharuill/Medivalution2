from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, TextAreaField, Form
from wtforms.fields.simple import EmailField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  username = StringField('Username', [validators.Length(min=4, max=25)])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
  username = StringField('Username', [validators.Length(min=4, max=25)])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  email = EmailField('Email',validators=[DataRequired()])
  submit = SubmitField('Sign In')

class ChatForm(FlaskForm):
    username = StringField('Full Name', [validators.Length(min=4, max=25)])
    email = EmailField('Email Address', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Sign In')
