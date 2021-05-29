source venv/bin/activate
export FLASK_APP=aeocb.py
export FLASK_DEBUG=1
flask db migrate
flask db upgrade
