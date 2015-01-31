from flask import Flask
from .md_stories import md_stories

application = Flask(__name__)
application.debug = False

application.register_blueprint(md_stories, url_prefix='/stories')

application.secret_key = 'local-only-secret'

from app import views

