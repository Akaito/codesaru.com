"""
	csarucom.frontend
	~~~~~~~~~~~~~~~~~

	launchpad frontend application package
"""

from .. import factory


def create_app(settings_override=None):
	"""Returns the codesaru.com application instance"""
	app = factory.create_app(__name__, __path__, settings_override)

	# Register custom error handlers
	if not app.debug:
		for e in (404, 500):
			app.errorhandler(e)(handle_error)

	return app


def handle_error(e):
	#return render_template('errors/%s.html' % e.code), e.code
	abort(e)
