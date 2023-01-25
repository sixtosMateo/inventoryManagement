'''
Deployment:

When developing locally problaby using built-in development server, debugger and
reloader
    - Should use a dedicated WSGI server or hosting platform
'''

'''
Self-Hosted Options
- Flask is WSGI Application
- A WSGI server is used to run the application
    - Converting incoming HTTP requests to the standard WSGI environ
    - and converting outgoing WSGI responses to HTTP responses
'''

'''
Goal of the tutorial is to familiarize with the concepts involved in running WSGI
application using a production WSGI server and HTTP server

There are many WSGI servers and HTTP servers:
Below are common servers and show the basics of running each one
    Gunicorn
    Waitress
    mod_wsgi
    uWSGI
    gevent
    eventlet
    ASGI

WSGI servers have HTTP servers built-in
    - however a dedicated HTTP server maybe be safer, more efficient or more
    capable
    - Putting an HTTP server infront of the WSGI server is called Reverse Proxy
        - nginx
        - Apache httpd
'''

'''
Hosting Platform:
Many services for hosting web applications without needing to maintain own server,
nertwoking, domain.
    - Some have free tier up to a certain time or bandwidth

Common Platforms which have instructions for Flask, WSGI or Python
    - PythonAnywhere
    - Google App Engine
    - Google Cloud Run
    - AWS Elastic Beanstalk
    - Microsoft Azure
'''
