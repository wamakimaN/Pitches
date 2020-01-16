from flask import Flask, render_template,request,redirect,url_for,abort
from ..models import Idea,User
from flask_login import login_required,current_user
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from . import main
from .form import IdeaForm
from .. import db

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    

    return render_template('index.html')

@main.route('/user/<uname>', methods = ['GET','POST'])
@login_required
def profile(uname):

    form = IdeaForm()
    user = User.query.filter_by(username = uname).first()
    ideas = Idea.query.all()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data

        
        new_idea = Idea(title=form.title.data,body=form.body.data,owner = current_user)
        
        db.session.add(new_idea)
        db.session.commit()
                            
    

    return render_template("profile/profile.html",ideas = ideas, user = user,idea_form = form)


    