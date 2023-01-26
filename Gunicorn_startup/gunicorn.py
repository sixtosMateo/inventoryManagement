'''
Getting Started with Gunicorn
$ cd hello-app
$ python -m venv venv
$ . venv/bin/activate
$ pip install .  # install your application
$ pip install gunicorn

Syntax:
    {module_import}:{app_variable}
    gunicorn -w 4 'hello:app'
    gunicorn -w 4 'hello:create_app()'

Binding Externally:
    gunicorn -w 4 -b 0.0.0.0 'hello:create_app()'
'''
