from flask import abort, Blueprint, flash, Markup, render_template
import json
from markdown import markdown
from os import path, walk

md_stories = Blueprint('md_stories', __name__,
	template_folder='templates'
)

content_dir = path.join(md_stories.root_path, 'content')
stories_dir = path.join(content_dir, 'stories')

stories = {}

class MdStory():
	def __init__(self):
		self.md = None
		self.title = None
		self.date = None

	@classmethod
	def from_json(cls, jsn):
		obj = cls()
		obj.md = Markup(markdown(open(jsn['content']).read()))
		obj.title = jsn['title']
		obj.date = jsn['date']
		return obj

def collect_stories():
	index_data = json.load(open(path.join(stories_dir, 'index.json')))
	for story in index_data['stories']:
		if not story['enabled']:
			continue
		story['content'] = path.join(stories_dir, story['content'])
		stories[story['path']] = MdStory.from_json(story)
	pass

collect_stories()

@md_stories.route('/')
def route_stories():
	#collect_stories()
	return render_template(
		'stories.html',
		breadcrumbs=[{'path': '/', 'text': 'Home'}],
		md_stories_root_path=md_stories.root_path,
		stories=stories
	)

@md_stories.route('/<story>')
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

