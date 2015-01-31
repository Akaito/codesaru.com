from flask import abort, Blueprint, flash, Markup, render_template
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

class MdStory():
	def __init__(self):
		self.md = None
		self.title = None
		self.date_begin = None
		self.date_end = None
		self.date_release = None

	@classmethod
	def from_json(cls, jsn):
		obj = cls()
		obj.md = Markup(markdown(open(jsn['content']).read()))
		obj.title = jsn['title']
		obj.date_begin = jsn['date-begin']
		obj.date_end = jsn['date-end']
		obj.date_release = jsn['date-release']
		return obj

def collect_projects():
	index_data = json.load(open(path.join(projects_dir, 'index.json')))
	for project in index_data['projects']:
		if not project['enabled']:
			continue
		project['content'] = path.join(projects_dir, project['content'])
		projects[project['path']] = MdStory.from_json(project)
	pass

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

@md_projects.route('/<project>')
def route_project(project):
	#collect_projects()
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
		content=md_project.md
	)

