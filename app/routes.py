from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

from app.forms import ResetPasswordRequestForm, PostForm, ThemeForm
from app.email import send_password_reset_email

from app.forms import ResetPasswordForm
from app.models import Post, Theme, UserRoles, Country, UserCountries



@app.route('/')
@app.route('/index')
def index():
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)      
        db.session.commit()
        user_role = UserRoles(user_id=user.id , role_id=1)
        db.session.add(user_role)  
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

@app.route('/posts/', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(english = form.english.data, french = form.french.data, kirundi = form.kirundi.data, final_text = form.final_text.data, post_type = form.post_type.data, hashtag = form.hashtag.data, user_id = current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Congratulations, you have added new post!')
        return redirect(url_for('index'))
    return render_template('add_post.html', title='Add Post', form=form)


@app.route('/posts/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.filter_by(id = post_id).first_or_404()
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.english = form.english.data
        post.french = form.french.data
        post.kirundi = form.kirundi.data
        post.final_text = form.final_text.data
        post.post_type = form.post_type.data
        post.hashtag = form.hashtag.data
        post.user_id = current_user.id
        db.session.commit()
        flash('Congratulations, you have edited the post!')
        return redirect(url_for('index'))
    return render_template('add_post.html', title='Edit Post', form=form)

@app.route('/themes/', methods=['GET', 'POST'])
def add_theme():
    form = ThemeForm()
    if form.validate_on_submit():
        theme = Theme(theme_from_date = form.theme_from_date.data, theme_to_date = form.theme_to_date.data, theme = form.theme.data, theme_hashtag = form.theme_hashtag.data, user_id = current_user.id)
        db.session.add(theme)
        db.session.commit()
        flash('Congratulations, you have added new Theme!')
        return redirect(url_for('index'))
    return render_template('add_theme.html', title='Add Theme', form=form)


@app.route('/themes/<int:theme_id>', methods=['GET', 'POST'])
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