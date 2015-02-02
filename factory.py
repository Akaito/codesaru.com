from os import path, walk

from flask import Flask

from .helpers import register_blueprints


def create_app(package_name, package_path, settings_override=None):
	app = Flask(package_name, instance_relative_config=True)

	app.config.from_object('csarucom.settings')

	# discover what blueprint packages may be present
	blueprint_dirs = package_path
	for root, dirs, files in walk(path.join(package_path[0], 'blueprints')):
		for dir in dirs:
			blueprint_dirs.append(path.join(root, dir))
			print('going to discover %s' % blueprint_dirs[-1])
		break
	# attempt to find all Blueprints within those packages and register them
	register_blueprints(app, package_name, blueprint_dirs)

	return app
