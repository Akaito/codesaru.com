"""
	csarucom.main (init)
	~~~~~~~~~~~~~

	Index route.
"""

from flask import Blueprint, render_template

from ... import route
from .. import stories as stories_plugin
from .. import projects as projects_plugin


bp = Blueprint('bpmain', __name__, template_folder='templates')

@route(bp, '/')
def index():
	return render_template('main-test.html', stories_plugin=stories_plugin, projects_plugin=projects_plugin)
	return render_template('index.html')
