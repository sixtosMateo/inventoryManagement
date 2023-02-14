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

'''Compare to auth blueprint blog bp does not have a url prefix'''
bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
