from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[Required(),Email()])
    pass_secure = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')