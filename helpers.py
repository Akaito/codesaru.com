import pkgutil
import importlib
from runpy import run_module # testing
from os import path # testing

from flask import Blueprint

#from .main.plugins import fa

def register_blueprints(app, package_name, blueprint_dirs):
	"""Register all Blueprints found in all modules.

	This, and much other app structure-oriented code, comes from
	http://mattupstate.com/python/2013/06/26/how-i-structure-my-flask-applications.html
	https://github.com/mattupstate/overholt
	"""
	blueprints = []
	if False:
		#for _, name, ispkg in pkgutil.walk_packages(blueprint_dirs):
		for _, name, ispkg in pkgutil.iter_modules(blueprint_dirs):
			print('iter mod: %s (ispkg? %s)' % (name, ispkg))
			#import name
			print('m = import_module(%s.%s)' % (package_name, name))
			m = importlib.import_module('%s.%s' % (package_name, name))
			for item in dir(m):
				item = getattr(m, item)
				if isinstance(item, Blueprint):
					app.register_blueprint(item)
					print("Registered a blueprint! (%s)" % name)
				blueprints.append(item)
	elif False:
		for pkg_dir in blueprint_dirs:
			pkg_name = path.split(pkg_dir)[-1]
			print('pkg_dir: %s -- named %s' % (pkg_dir, pkg_name))
			run_module(pkg_name)
	else:
		print('name %s' % __name__)
		#m = importlib.import_module('csarucom.main.plugins.n')
		m = importlib.import_module('.plugins.n', 'csarucom.main')
		for item in dir(m):
			item = getattr(m, item)
			if isinstance(item, Blueprint):
				app.register_blueprint(item)
				#print("Registered a blueprint! (%s)" % name)
			blueprints.append(item)
	return blueprints
