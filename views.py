from flask import flash, render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/test')
def test():
	flash('Hello,')
	flash('world')
	return render_template('index.html')
