"""
	csarucom.bptest main code
"""

from flask import Blueprint

from . import route

bp = Blueprint('bptest', __name__)

@route(bp, '/t')
def route_t():
	return 'test'
