from flask import Blueprint, render_template
#from . import route

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
	return 'main index'
