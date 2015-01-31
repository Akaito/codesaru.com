import flask
app = flask.Flask(__name__)
app.debug = False
app.secret_key = 'local-only-secret'

from app.views import main

