from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    items = ['apple', 'banana', 'celebi', (40+2)]
    return render_template(
        'index.html',
        item_list = items
    )

@app.route('/old/upcheck.php')
def old_upcheck():
    return render_template(
        'old/upcheck.xml',
        upgrade_available = 0,
        description       = 'foo',
        base_version      = 'blah',
        target_version    = 'INVALID',
        motd              = 'message here',
        links             = [
            { 'name': 'google', 'url': 'http://google.com/'        },
            { 'name': 'nr',     'url': 'http://nitronic-rush.com/' }
        ]
    )

@app.route('/old/score_get.php')
def old_score_get():
# If failed, pass in a 'desc', set 'style' to 7, and give a None scores list
# Style 6: score-based, style 7: time-based
    return render_template(
        'old/score_get.xml',
        style = 7,
        level_id = 42,
        scores = [
            {
                'initials': 'AAA',
                'time': 10.2,
                'score': 42,
                'biggest_trick': 8,
                'date': '2014-01-01',
                'id': 853
            },
            {
                'initials': 'FOO',
                'time': 10.2,
                'score': 42,
                'biggest_trick': 8,
                'date': '2014-01-01',
                'id': 853
            }
        ],
        desc = None
    )

@app.route('/old/ghost_get.php')
def old_ghost_get(bin_data=None):
    if bin_data is not None:
        return bin_data
    return render_template(
        'old/ghost_get.xml',
        score_id = 4,
        desc = 'foo'
    )

@app.route('/old/score_upload_with_ghost.php')
def old_ghost_upload():
    return render_template(
        'old/score_upload_with_ghost.xml',
        success  = 1,
        score_id = 4,
        desc     = None
    )

