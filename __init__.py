from flask import Flask
from .module_stories import md_stories
from .module_projects import md_projects

application = Flask(__name__)
application.debug = False

application.register_blueprint(md_stories, url_prefix='/stories')
application.register_blueprint(md_projects, url_prefix='/projects')

application.secret_key = 'local-only-secret'

from app import views

