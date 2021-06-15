"""empty message

Revision ID: 47e033dc64f4
Revises: 
Create Date: 2021-06-06 18:54:48.500026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47e033dc64f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('code', sa.String(length=3), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('name')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('theme',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('theme_from_date', sa.Date(), nullable=True),
    sa.Column('theme_to_date', sa.Date(), nullable=True),
    sa.Column('theme', sa.String(), nullable=True),
    sa.Column('theme_hashtag', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_theme_timestamp'), 'theme', ['timestamp'], unique=False)
    op.create_table('user_countries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('language_1', sa.String(), nullable=True),
    sa.Column('language_2', sa.String(), nullable=True),
    sa.Column('language_3', sa.String(), nullable=True),
    sa.Column('final_text', sa.String(), nullable=True),
    sa.Column('hashtag', sa.String(), nullable=True),
    sa.Column('post_image_url', sa.String(), nullable=True),
    sa.Column('post_date_time', sa.DateTime(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('theme_id', sa.Integer(), nullable=True),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.Column('post_status', sa.String(), nullable=True),
    sa.Column('post_type', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.ForeignKeyConstraint(['theme_id'], ['theme.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.create_table('theme_countries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('theme_id', sa.Integer(), nullable=True),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['theme_id'], ['theme.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_countries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_countries')
    op.drop_table('theme_countries')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_table('user_roles')
    op.drop_table('user_countries')
    op.drop_index(op.f('ix_theme_timestamp'), table_name='theme')
    op.drop_table('theme')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('country')
    # ### end Alembic commands ###