from flask import render_template,redirect,url_for
from flask_wtf import FlaskForm
from ..models import User
from . import auth
from .form import LoginForm,RegistrationForm
from .. import db


@auth.route('/login',methods = ['GET','POST'])
def login():

    form = LoginForm()

    return render_template('auth/login.html', form = form)

@auth.route('/signup',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,pass_secure = form.pass_secure.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/signup.html',form = form)