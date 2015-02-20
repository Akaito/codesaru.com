"""
	csarucom.main (init)
	~~~~~~~~~~~~~

	Index route.
"""

from flask import Blueprint, render_template

from ... import route


bp = Blueprint('bpmain', __name__, template_folder='templates')
#print(' -- MAIN BP')

@route(bp, '/')
def index():
	#print(' VISITED /')
	return render_template('main-test.html')
	return render_template('test.html')
