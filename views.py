from flask import abort, flash, render_template
from app import app

class Breadcrumb():
	def __init__(self, text, path):
		self.text = text
		self.path = path
class Breadcrumbs():
	def __init__(self, other=None):
		self.crumbs = []
		if other:
			for crumb in other.crumbs:
				self.crumbs.append(crumb)
	def add_crumb(self, text, path=None):
		self.crumbs.append({'text': text, 'path': path})
		return self
	def get_html(self):
		result = ''
		for crumb in self.crumbs[:-1]:
			if crumb.path:
				result += '<li><a href="%s">%s</a></li>' % (crumb.path, crumb.text)
			else:
				result += '<li>%s</li>' % crumb.text
		result += '<li>%s</li>' % self.crumbs[-1]
		return result

index_crumbs = Breadcrumbs().add_crumb('Home', '/')

@app.route('/')
@app.route('/index')
def index():
	return render_template(
		'index.html',
		breadcrumbs=None
	)

@app.route('/story/account-less-online-friend-oriented-leaderboards')
def story_account_less_leaderboards():
	return render_template(
		'story/account-less-online-friend-oriented-leaderboards.html',
		breadcrumbs=Breadcrumbs(index_crumbs)
	)

@app.route('/test')
def test():
	flash('Hello,')
	flash('world')
	return render_template('index.html')
