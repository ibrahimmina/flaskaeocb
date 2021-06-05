from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField,FileField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import app, db
from app.models import Post, Theme, UserRoles, Country, UserCountries, PostType

class PostForm(FlaskForm):
    post_date_time = DateField('post_date_time', validators=[DataRequired()])
    language_1 = StringField('language_1')
    language_2 = StringField('language_2')
    language_3 = StringField('language_3')
    final_text = StringField('Final Text')
    post_type = QuerySelectField('Post Type', query_factory=PostType.query.all())
    hashtag = StringField('hashtag')
    post_image_url = FileField('Post Image')
    submit = SubmitField('Add/Edit Post')

class ThemeForm(FlaskForm):

    theme_from_date = DateField('theme_from_date', validators=[DataRequired()])
    theme_to_date = DateField('theme_to_date', validators=[DataRequired()])
    theme = StringField('theme', validators=[DataRequired()])
    theme_hashtag = StringField('theme_hashtag', validators=[DataRequired()])
    submit = SubmitField('Add Theme')

def post_type_choices():      
    return db.session.query(PostType).all()



