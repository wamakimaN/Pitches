from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import Idea

class IdeaForm(FlaskForm):
    title = StringField('What is you idea about?',validators=[Required()])
    body = TextAreaField('Tell us more.')
    submit = SubmitField('Submit')