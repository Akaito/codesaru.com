from flask import Blueprint

from .main.main import bp as mainbp

def register_blueprints(app, package_name, package_path):
	app.register_blueprint(mainbp)
