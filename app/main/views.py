from flask import Flask, render_template,request,redirect,url_for,abort
from ..models import Idea,User
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from . import main

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)