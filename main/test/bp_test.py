"""
	csarucom.bp_test test Blueprint
"""

from flask import Blueprint, render_template

from . import route

bp = Blueprint('bptest', __name__, template_folder='templates', static_folder='static', static_url_path='/static/test')

@route(bp, '/test')
def route_t():
	return render_template('test.html')
