from flask import render_template
from flask_login import login_required
from app.models import Post, Theme, UserRoles, Country, UserCountries

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html')

@home.route('/country/<int:country_id>')
def countryPage(country_id):
    """
    Render the homepage template on the / route
    """
    country_post = Post.query.filter_by(country_id=country_id).all()
    return render_template('home/country_post.html', title='Country Posts', country_post=country_post)
