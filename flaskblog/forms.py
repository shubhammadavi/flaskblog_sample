from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class ResgistrationForm(FlaskForm):
  username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
  email = EmailField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm password', validators=[DataRequired(),EqualTo('password')])
  submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
  email = EmailField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')