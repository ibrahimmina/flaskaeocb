from flask import render_template
from flask_login import login_required

from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

from app.forms import ResetPasswordRequestForm
from app.admin.forms import PostForm, ThemeForm
from app.email import send_password_reset_email

from app.forms import ResetPasswordForm
from app.models import Post, Theme, UserRoles, Country, UserCountries

from . import admin


@admin.route('/')
@login_required
def homepage():
    """
    Render the homepage template on the / route
    """
    user = {'username': 'French Cluster'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='Home Page', posts=posts) 


@admin.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)



@admin.route('/posts/', methods=['GET', 'POST'])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post( 
        post_date_time = form.post_date_time.data ,
        language_1 = form.language_1.data ,
        language_2 = form.language_2.data ,      
        language_3 = form.language_3.data ,      
        final_text = form.final_text.data ,      
        hashtag = form.hashtag.data ,
        user_id = current_user.id,
        post_image_url="",
        theme_id=1,
        country_id=43,
        post_status_id=1,
        post_type_id=1)
        db.session.add(post)
        db.session.commit()
        flash('Congratulations, you have added new post!')
        return redirect(url_for('index'))
    return render_template('add_post.html', title='Add Post', form=form)


@admin.route('/posts/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.filter_by(id = post_id).first_or_404()
    form = PostForm(obj=post)
    if form.validate_on_submit():

        post_date_time = form.post_date_time.data
        language_1 = form.language_1.data
        language_2 = form.language_2.data 
        language_3 = form.language_3.data 
        final_text = form.final_text.data 
        hashtag = form.hashtag.data 
        user_id = current_user.id
        post_image_url=""
        theme_id=1
        country_id=43
        post_status_id=1
        post_type_id=1
        db.session.commit()
        flash('Congratulations, you have edited the post!')
        return redirect(url_for('index'))
    return render_template('add_post.html', title='Edit Post', form=form)

@admin.route('/themes/', methods=['GET', 'POST'])
@login_required
def add_theme():
    form = ThemeForm()
    if form.validate_on_submit():
        theme = Theme(theme_from_date = form.theme_from_date.data, theme_to_date = form.theme_to_date.data, theme = form.theme.data, theme_hashtag = form.theme_hashtag.data, user_id = current_user.id)
        db.session.add(theme)
        db.session.commit()
        flash('Congratulations, you have added new Theme!')
        return redirect(url_for('index'))
    return render_template('add_theme.html', title='Add Theme', form=form)


@admin.route('/themes/<int:theme_id>', methods=['GET', 'POST'])
@login_required
def edit_theme(theme_id):
    theme = Theme.query.filter_by(id = theme_id).first_or_404()
    form = ThemeForm(obj=theme)
    if form.validate_on_submit():
        theme.theme_from_date = form.theme_from_date.data 
        theme.theme_to_date = form.theme_to_date.data
        theme.theme = form.theme.data
        theme.theme_hashtag = form.theme_hashtag.data 
        theme.user_id = current_user.id
        db.session.commit()
        flash('Congratulations, you have edited the Theme!')
        return redirect(url_for('index'))
    return render_template('add_theme.html', title='Edit Theme', form=form)

