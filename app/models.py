from datetime import datetime
from app import app, db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
import jwt
from hashlib import md5
from time import time
from flask import url_for


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    themes = db.relationship('Theme', backref='user', lazy=True)
    posts = db.relationship('Post', backref='user', lazy=True)
    roles = db.relationship('Role', secondary='user_roles',
            backref=db.backref('users', lazy='dynamic'))
    countries = db.relationship('Country', secondary='user_countries',
            backref=db.backref('users', lazy='dynamic'))

    def to_dict(self, include_email=False, include_themes=False, include_roles=False):
        data = {
            'id': self.id,
            'username': self.username,
        }
        if include_email:
            data['email'] = self.email
        return data

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))            

# Define Role model
class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
        }
        return data

# Define UserRoles model
class UserRoles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

    def to_dict(self):
        data = {
            'id': self.id,
            'user_id': self.user_id,
            'role_id': self.role_id,
        }
        return data

# Define Role model
class Country(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    code = db.Column(db.String(3), unique=True)
    status = db.Column(db.Integer())

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'status': self.status,            
        }
        return data

# Define UserRoles model
class UserCountries(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    country_id = db.Column(db.Integer(), db.ForeignKey('country.id', ondelete='CASCADE'))

    def to_dict(self):
        data = {
            'id': self.id,
            'user_id': self.user_id,
            'country_id': self.country_id,         
        }
        return data

# Define UserRoles model
class PostCountries(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id', ondelete='CASCADE'))
    country_id = db.Column(db.Integer(), db.ForeignKey('country.id', ondelete='CASCADE'))

    def to_dict(self):
        data = {
            'id': self.id,
            'post_id': self.post_id,
            'country_id': self.country_id,         
        }
        return data

# Define UserRoles model
class ThemeCountries(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    theme_id = db.Column(db.Integer(), db.ForeignKey('theme.id', ondelete='CASCADE'))
    country_id = db.Column(db.Integer(), db.ForeignKey('country.id', ondelete='CASCADE'))

    def to_dict(self):
        data = {
            'id': self.id,
            'theme_id': self.theme_id,
            'country_id': self.country_id,         
        }
        return data


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language_1 = db.Column(db.String)
    language_2 = db.Column(db.String)
    language_3 = db.Column(db.String)
    final_text = db.Column(db.String)
    hashtag = db.Column(db.String)
    post_image_url = db.Column(db.String)
    post_date_time = db.Column(db.DateTime)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    theme_id = db.Column(db.Integer, db.ForeignKey('theme.id'))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    post_status = db.Column(db.String)
    post_type= db.Column(db.String)

    def to_dict(self):
        data = {
            'id': self.id,
            'theme_id': self.theme_id,
            'country_id': self.country_id,         
        }
        return data

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Theme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme_from_date = db.Column(db.Date)
    theme_to_date = db.Column(db.Date)
    theme = db.Column(db.String)
    theme_hashtag = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    countries = db.relationship('Country', secondary='theme_countries',
            backref=db.backref('themes', lazy='dynamic'))    

    def __repr__(self):
        return '<Theme {}>'.format(self.body)


