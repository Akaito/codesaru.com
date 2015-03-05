"""
	csarucom.bp_test test Blueprint
"""

from flask import Blueprint, render_template

#print('TEST TEST')

from ... import route

bp = Blueprint(
	'test',
	__name__,
	template_folder='templates',
	static_folder='static',
	static_url_path='/static/test'
)

@route(bp, '/test')
def route_t():
	#return render_template('main-test.html')
	return render_template('test.html')
