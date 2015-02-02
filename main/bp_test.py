"""
	csarucom.bp_test test Blueprint
"""

from flask import Blueprint

from . import route

bp = Blueprint('bptest', __name__)

@route(bp, '/test')
def route_t():
	return 'test'
