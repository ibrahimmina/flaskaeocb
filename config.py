import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

	SQLALCHEMY_DATABASE_URI = 'postgresql://debian:debian@localhost/aeocb'
    
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	MAIL_SERVER='smtp.gmail.com'
	MAIL_PORT= 465
	MAIL_USE_SSL = True
	MAIL_USERNAME= 'visum360@gmail.com'
	MAIL_PASSWORD= 'bbmqyhtwikcnjunv'
