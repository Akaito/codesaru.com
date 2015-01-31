import os
from flask import abort, Blueprint, flash, Markup, render_template
from jinja2 import TemplateNotFound
from markdown import markdown
from app import application

index_crumbs = [{'text': 'Home', 'path': '/'}]

@application.route('/')
@application.route('/index')
def index():
	return render_template(
		'index.html'
	)

@application.route('/story/account-less-online-friend-oriented-leaderboards')
def story_account_less_leaderboards():
	return render_template(
		'story/account-less-online-friend-oriented-leaderboards.html',
		breadcrumbs=index_crumbs
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
