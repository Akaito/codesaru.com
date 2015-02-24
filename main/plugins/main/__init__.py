"""
	csarucom.main (init)
	~~~~~~~~~~~~~

	Index route.
"""

from flask import Blueprint, render_template

from ... import route


bp = Blueprint('bpmain', __name__, template_folder='templates')

@route(bp, '/')
def index():
	return render_template('main-test.html')
	return render_template('index.html')
