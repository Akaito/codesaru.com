from flask import abort, Blueprint, flash, Markup, render_template, url_for
import json
from markdown import markdown
from os import path, walk

md_projects = Blueprint('md_projects', __name__,
	template_folder='templates',
	static_folder='static'
)

content_dir = path.join(md_projects.root_path, 'content')
projects_dir = path.join(content_dir, 'projects')

projects = {}
projects_sorted = []

class MdStory():
	def __init__(self):
		self.md = None
		self.title = None
		self.date_begin = None
		self.date_end = None
		self.date_release = None
		self.image_main = None
		self.images = []

	@classmethod
	def from_json(cls, jsn):
		obj = cls()
		obj.md = Markup(markdown(open(jsn['content']).read()))
		obj.path = jsn['path']
		obj.title = jsn['title']
		obj.date_begin = jsn['date-begin']
		obj.date_end = jsn['date-end']
		obj.date_release = jsn['date-release']
		obj.image_main = jsn['image-main']
		obj.images = []
		for img in jsn['images']:
			obj.images.append(img)
		return obj

	def has_images(self):
		return self.image_main is not None and len(self.image_main) > 0

	def image_main_url(self, thumb):
		return url_for(
			'.static',
			filename='%s%s/%s' % (
				self.path,
				'/thumbs' if thumb else '',
				self.image_main
			)
		)

	def images_count(self):
		return len(self.images)

	def image_url(self, i, thumb):
		return url_for(
			'.static',
			filename='%s%s/%s' % (
				self.path,
				'/thumbs' if thumb else '',
				self.images[i]
			)
		)

def collect_projects():
	global projects, projects_sorted
	projects = {}
	projects_sorted = []
	index_data = json.load(open(path.join(projects_dir, 'index.json')))
	for project in index_data['projects']:
		if not project['enabled']:
			continue
		project['content'] = path.join(projects_dir, project['content'])
		projects_sorted.append(MdStory.from_json(project))
		projects[project['path']] = projects_sorted[-1]

def get_items():
	return projects_sorted

collect_projects()

@md_projects.route('/')
def route_projects():
	#collect_projects()
	return render_template(
		'projects.html',
		breadcrumbs=[{'path': '/', 'text': 'Home'}],
		md_projects_root_path=md_projects.root_path,
		projects=projects
	)

@md_projects.route('/t')
def route_t():
	return md_projects.send_static_file('nitronic-rush/story_mode_flight_thumb_0.png')

@md_projects.route('/<string:project>')
def route_project(project):
	#collect_projects()
	if '..' in project or project.startswith('/'):
		abort(404)
	if project not in projects:
		abort(404)
	md_project = projects[project]
	return render_template(
		'project.html',
		breadcrumbs=[
			{'path': '/', 'text': 'Home'},
			{'path': '/projects', 'text': 'Projects'}
		],
		title=md_project.title,
		date_begin=md_project.date_begin.split('-')[0],
		date_end=md_project.date_end.split('-')[0],
		date_release=md_project.date_release,
		content=md_project.md,
		proj=md_project
	)

