'''
Gunicorn is a pure WSGI server with simple configuration and multiple worker
implementations for performance tuning
    - it tends to integrate easily with hosting applications
    - it does not support Windows (but does run on WSL)
    - it is easy to install as it does not require dependencies or compilation
    - it has built-in async worker support using gevent and eventlet

Running
The only required argument to Gunicorn tells it how to load your flask application

Syntax {module_import}:{app_variable}

- {module_import} is the dotted import name to the module with your application
- {app_variable} is the variable with the application
    - it can also be a function call (with any arguments) if your using the
    app factory pattern

# equivalent to 'from hello import app'
$ gunicorn -w 4 'hello:app'

# equivalent to 'from hello import create_app; create_app()'
$ gunicorn -w 4 'hello:create_app()'
'''
