'''
Flask Tutorial App: Flaskr
Created By: Mateo Sixtos
Date: 1/30/23
Description: Blog application. Users are able to register, log in, create post,
edit or delete their own post. This application will be able to be package and
can be install on other computers.
'''

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)
