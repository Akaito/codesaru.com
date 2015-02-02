from flask import Blueprint, current_app, render_template

from . import route

bp = Blueprint('bpmain', __name__)

@route(bp, '/')
def index():
	return render_template('index.html')
	return render_template('test.html')
