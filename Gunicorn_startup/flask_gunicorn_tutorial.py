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

The -w option specifies the number of processes to run
    - a starting value could be CPU*2
    - the default value is only 1 worker which is probably not what you want for
    the default worker type

Logs
    - logs for each request arent shown by default only worker info and errors are
    shown
    To show access logs on std-out use the --access-logfile=-option

Binding Externally
    - Gunicorn should not be run as root because it would cause your application
    code to run as root which is not secure
        - it means it will not be possible to bind to port 80 or 443
        - instead a reverse proxy such as nginx or apache httpd should be used
        infront of Gunicorn

    - You can bind to all external IPs on a non-privileged port using -b 0.0.0.0
    option
    - Do not do this when using a reverse proxy setup otherwise it will be possible
    to bypass the proxy

EX:
    gunicorn -w 4 -b 0.0.0.0 'hello:create_app()'
    Listening at: http://0.0.0.0:8000 (x)

0.0.0.0 is not a valid address to navigate to, you'd use a specific IP address in your
browser

'''
