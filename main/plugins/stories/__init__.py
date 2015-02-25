"""
	csarucom.stories (init)
	~~~~~~~~~~~~~
"""

from os import path, walk
import json

from flask import abort, Blueprint, flash, Markup, render_template
from markdown import markdown

from ... import route

md_stories = Blueprint(
	'md_stories',
	__name__,
	template_folder='templates',
	static_folder='static'
)

content_dir = path.join(md_stories.root_path, 'content')
stories_dir = path.join(content_dir, 'stories')

stories = {}
stories_sorted = []

class MdStory():
	def __init__(self):
		self.path = None
		self.md = None
		self.title = None
		self.date = None

	@classmethod
	def from_json(cls, jsn):
		obj = cls()
		obj.path = jsn['path']
		obj.md = Markup(markdown(open(jsn['content']).read()))
		obj.title = jsn['title']
		obj.date = jsn['date']
		return obj

def collect_stories():
	global stories, stories_sorted
	stories = {}
	stories_sorted = []
	index_data = json.load(open(path.join(stories_dir, 'index.json')))
	for story in index_data['stories']:
		if not story['enabled']:
			continue
		story['content'] = path.join(stories_dir, story['content'])
		stories_sorted.append(MdStory.from_json(story))
		stories[story['path']] = stories_sorted[-1]

def get_items():
	return stories_sorted

collect_stories()

@route(md_stories, '/stories/') # TODO : Plugin-finder makes '/' mean '/stories/'
def route_stories():
	#collect_stories()
	return render_template(
		'stories.html',
		breadcrumbs=[{'path': '/', 'text': 'Home'}],
		md_stories_root_path=md_stories.root_path,
		stories=stories
	)

@md_stories.route('/stories/<story>')
def route_story(story):
	#collect_stories()
	if story not in stories:
		abort(404)
	md_story = stories[story]
	return render_template(
		'story.html',
		breadcrumbs=[
			{'path': '/', 'text': 'Home'},
			{'path': '/stories', 'text': 'Stories'}
		],
		title=md_story.title,
		date=md_story.date,
		content=md_story.md
	)

