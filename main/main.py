from flask import Blueprint #, render_template

from . import route

bp = Blueprint('bpmain', __name__)

@route(bp, '/')
def index():
	return 'main index'
