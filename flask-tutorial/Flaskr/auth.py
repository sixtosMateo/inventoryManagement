import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

'''__name__ arg
    - Like the application object, the blueprint needs to know where it is
    defined so __name__ is passed as the second argument
'''
'''bp is the blueprint for authentication view logic'''
bp = Blueprint('auth', __name__, url_prefix='/auth')

'''
bp.route associates the URL /register with the register view function

After storing the user, they are redirected to the login page

url_for() generates the URL for the login view based on its name
    - This is preferable to writing the url directly as it allows you to change
    the URL later without changing all code that links to it
    - redirect() generates a redirect respinse to the generated URL
'''

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

'''
check_password_hash: hashes the submitted password and securely compares them

session is a dict that stores data across requests
    - when the validation succeeds the user's id is stored in a new session
    - The data is stored in a cookie that is sent to the browser and the browser
    then sends it back with subsequent requests
    - Flask securely signs the data so that it cant be tampered with

Now that the user's id is stored in the session, it will be available on subsequent
requests
    - At the beginning of each request, if a user is logged in their information
    should be loaded and made available to other views
'''
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

'''
before_app_request() registers a function that runs before the view function no
matter what URL is requested

load_logged_in_user() checks if a user id is stored in the session and gets the
users data from the database
    - storing it on g.user which lasts for the length of the request, if there
    is no user id or if the id doesnt exist g.user will be none
'''
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

'''
To log out you need to remove user_id from the session. This prevents
load_logged_in_user function to load a user info on subsequent requests
'''
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
