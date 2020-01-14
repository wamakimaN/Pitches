from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[Required(),Email()])
    pass_secure = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    pass_secure = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')