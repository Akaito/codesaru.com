'''
*  Finds and registers blueprints in plugin directories.
'''

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
	if True:
		for plugin_dir in blueprint_dirs:
			plugin_name = path.split(plugin_dir)[-1]
			#print('plugin_dir: %s -- name %s' % (plugin_dir, plugin_name))
			m = importlib.import_module('.plugins.%s' % plugin_name, 'csarucom.main')
			if m is None:
				continue

			for item in dir(m):
				item = getattr(m, item)
				if isinstance(item, Blueprint):
					app.register_blueprint(item)
					print("Registered a blueprint (%s) from plugin (%s)" % (item, plugin_name))
				blueprints.append(item)
	return blueprints
