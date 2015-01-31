from flask import abort, Blueprint, flash, Markup, render_template
from jinja2 import TemplateNotFound
from markdown import markdown
from app import application

@application.route('/')
@application.route('/index')
def index():
	return render_template(
		'index.html'
	)

@application.route('/test')
def test():
	flash('Hello,')
	flash('world')
	return render_template(
		'index.html'
	)

@application.route('/m')
def m():
	return render_template(
		'index.html',
		scratch=Markup(markdown("""
Chapter
=======

Section
-------

[Google][]

* List 1
* List 2

[Google]: http://google.com/
		"""
		))
	)
