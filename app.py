from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("do_the_login")
        return None
        # return do_the_login()
    else:
        print("show_the_login_form")
        return None
        # return show_the_login_form()

"html escaping prevents injection attacks"
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

"variable section"
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

"trailing slashes"
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

"url building"
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='John Doe'))

"html rendering"

'''
Case 1: a module:
    /application.py
    /templates
        /hello.html

Case 2: a package:
    /application
        /__init__.py
        /templates
            /hello.html
'''
@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', name=name)

'''Context Locals and unit testing it'''
with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    print('Stating unit testing for request context')
    assert request.path == '/hello'
    assert request.method == 'POST'

'''Passing a whole environment'''
with app.request_context(environ):
    assert request.method == 'POST'
