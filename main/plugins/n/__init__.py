from flask import Blueprint

#print('N INIT')

from ... import route

bp = Blueprint(
	'n',
	__name__
)

@route(bp, '/n')
def route_n():
	return 'Nn'
