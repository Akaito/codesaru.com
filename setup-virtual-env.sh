#!/bin/bash

venvpy="virtualenv.py"
venvpysrc="https://raw.github.com/pypa/virtualenv/1.9.X/virtualenv.py"
venvdir="flask-env"
# Virtual environment setup script must be executable
if [ ! -x "$venvpy" ]; then
# TODO : Check for failure
    wget "$venvpysrc"
fi

# Create the virtual environment (if it's needed)
if [ ! -d "$venvdir" ]; then
# TODO : Check for failure
    python "$venvpy" "$venvdir"
fi

# Install our needed plugins for flask, jinja, etc. using pip
"$venvdir/bin/pip" install flask==0.9
"$venvdir/bin/pip" install flask-login
"$venvdir/bin/pip" install flask-openid
"$venvdir/bin/pip" install flask-mail==0.7.6
"$venvdir/bin/pip" install sqlalchemy==0.7.9
"$venvdir/bin/pip" install flask-sqlalchemy==0.16
"$venvdir/bin/pip" install sqlalchemy-migrate==0.7.2
"$venvdir/bin/pip" install flask-whooshalchemy==0.55a
"$venvdir/bin/pip" install flask-wtf==0.8.4
"$venvdir/bin/pip" install pytz==2013b
"$venvdir/bin/pip" install flask-babel==0.8
"$venvdir/bin/pip" install flup

