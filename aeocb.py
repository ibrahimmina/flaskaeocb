from app import app, db
from app.models import User, Post, Role, UserRoles, Theme


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Role': Role, 'UserRoles': UserRoles, 'Theme': Theme}