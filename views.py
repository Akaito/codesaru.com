from flask import abort, flash, render_template
from app import app, stories

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/story/account-less-online-friend-oriented-leaderboards')
def story_account_less_leaderboards():
	return render_template('story/account-less-online-friend-oriented-leaderboards.html')

@app.route('/test')
def test():
	flash('Hello,')
	flash('world')
	return render_template('index.html')
