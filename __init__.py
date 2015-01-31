from flask import Flask
from .md_stories import md_stories

app = Flask(__name__)
app.debug = False

app.register_blueprint(md_stories, url_prefix='/stories')

app.secret_key = 'local-only-secret'

from app.views import main

