from flask import Flask
from .helpers import register_blueprints

def create_app(package_name, package_path, settings_override=None):
	app = Flask(package_name, instance_relative_config=True)

	@app.route('/')
	def ind():
		return 'hi index'

	app.debug = True
	app.secret_key = 'its-a-secret'
	#app.config.from_object('my.settings')

	register_blueprints(app, package_name, package_path)

	return app
