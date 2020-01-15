from flask_login import login_user,logout_user,login_required
from flask import render_template,redirect,url_for,flash,request
from flask_wtf import FlaskForm
from ..models import User
from . import auth
from .form import LoginForm,RegistrationForm
from .. import db


@auth.route('/login',methods = ['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')


    return render_template('auth/login.html', form = form)

@auth.route('/signup',methods = ["GET","POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/signup.html',reg_form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
