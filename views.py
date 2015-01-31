from flask import flash, render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	flash('test')
	flash('another test')
	return render_template('index.html')

@app.route('/test')
def test():
	return 'Yay, it updated!'
