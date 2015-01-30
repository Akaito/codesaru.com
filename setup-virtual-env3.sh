#!/bin/bash

venvdir="flask-env"
# Create the virtual environment (if it's needed)
if [ ! -d "$venvdir" ]; then
# TODO : Check for failure
    python -m venv "$venvdir"
fi

# Install our needed plugins for flask, jinja, etc. using pip
"$venvdir/Scripts/pip" install flask
#"$venvdir/Scripts/pip" install flask-login
#"$venvdir/Scripts/pip" install flask-openid
#"$venvdir/Scripts/pip" install flask-mail==0.7.6
#"$venvdir/Scripts/pip" install sqlalchemy==0.7.9
#"$venvdir/Scripts/pip" install flask-sqlalchemy==0.16
#"$venvdir/Scripts/pip" install sqlalchemy-migrate==0.7.2
#"$venvdir/Scripts/pip" install flask-whooshalchemy==0.55a
#"$venvdir/Scripts/pip" install flask-wtf==0.8.4
#"$venvdir/Scripts/pip" install pytz==2013b
#"$venvdir/Scripts/pip" install flask-babel==0.8
#"$venvdir/Scripts/pip" install flup

