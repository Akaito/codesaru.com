from os import path

from flask import Flask

from .helpers import register_blueprints


def create_app(package_name, package_path, settings_override=None):
	app = Flask(package_name, instance_relative_config=True)

	app.config.from_object('csarucom.settings')

	# Find subdir modules (note: they'll be loaded into this main module)
	package_path.append(path.join(package_path[0], 'test'))

	#print('CREATE_APP(%s, %s, %s)' % (package_name, package_path, settings_override))
	register_blueprints(app, package_name, package_path)

	return app
