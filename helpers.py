import pkgutil
import importlib

from flask import Blueprint

def register_blueprints(app, package_name, package_path):
	"""Register all Blueprints found in all modules.

	This, and much other app structure-oriented code, comes from
	http://mattupstate.com/python/2013/06/26/how-i-structure-my-flask-applications.html
	https://github.com/mattupstate/overholt
	"""
	blueprints = []
	#print("register_blueprints(%s, %s, %s)" % (app, package_name, package_path))
	for _, name, _ in pkgutil.iter_modules(package_path):
		m = importlib.import_module('%s.%s' % (package_name, name))
		for item in dir(m):
			item = getattr(m, item)
			if isinstance(item, Blueprint):
				app.register_blueprint(item)
				print("Registered a blueprint! (%s)" % name)
			blueprints.append(item)
	return blueprints
