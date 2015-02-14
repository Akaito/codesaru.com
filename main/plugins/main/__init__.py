"""
	csarucom.main (init)
	~~~~~~~~~~~~~

	Index route.
"""

from flask import Blueprint, render_template

from ... import route


bp = Blueprint('bpmain', __name__)
print(' -- MAIN BP')

@route(bp, '/')
def index():
	print(' VISITED /')
	return render_template('index.html')
