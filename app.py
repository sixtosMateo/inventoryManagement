from flask import make_response
from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
from flask import session

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
    print('ending untit testing for request context')

'''Passing a whole environment'''
with app.request_context(environ):
    assert request.method == 'POST'

'''accepting data from form'''
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

'''Accessing url parameters not user friendly'''
searchword = request.args.get('key', '')


'''Uploading files'''


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...

'''secure_filename function save filename provided by client securely '''
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
    ...


'''Reading cookies.
    If wanting to use the session of cookie use the Sessions from Flask.
    Sessions adds security to towards client's cookie'''
@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.

'''Storing Cookies'''
@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

'''Setting cookie without response obj doesnt exist yet'''
'''utilize the deffered request callbacks pattern'''

'''Deffered Request Callbacks Pattern:
    One of the design principles of Flask is that response objects are created
    and passed down a chain of potential callbacks that can modify them or
    replace them.'''

'''Need to see about Response in Flask Documentation'''

'''Redirect and Errors'''

'''Redirect to another end point'''
@app.route('/')
def index():
    return redirect(url_for('login'))

'''to abort a request early with error code'''
@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


'''Response Objects: converting return values from view function into
                     response objects'''

'''wrapping response object from view int make response function'''
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

'''API JSON'''

'''coverting a dict or list return value from view into json response'''
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }


'''passing data to jsonify function. Function will serialize data if it is the
correct JSON data type: list and dictionary'''
app.route("/users")
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]

'''Complex types such as Database models there are serializable libraries and
API Extension that flask community maintaned that convert data to JSON valid
types '''



'''Sessions:
    Sessions objects allows you to store information specific to a user from one
    request to the next.
        - This is implemented on top of cookies with a cryptographic signature.
        - Users can look at the contents of the cookie but cannot modify it
        without the secret key used for signing
'''

# set secret key to some random bytes
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))



''' How to generate Secret Key
    Operating system has ways to generate random data based on cryptographic
    random generator

    Syntax
        python3 -c 'import secrets; print(secrets.token_hex())'''


'''Cookie based sessions:
    Flask take values you put into your session object and serialize them into
    a cookie.
    error use case:
        If some values dont persist across requests, cookies are indeed enable, 
        and you are not getting a clear error message
            -> check the size of your cookie in your page responses compared to
            the sized of the size supported by the web browser

    Besides the default client-side based sessions,
        if you want to handle sessions on the server side instead there are
        several flask extensions that support this
    '''
