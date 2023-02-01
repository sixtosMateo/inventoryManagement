'''
A Flask application is an instance of the Flask class.
    - everything about the application such as configuration and URLs will be
    registered with this class

Straightforward way to create a Flask application is to create a global Flask
instance directly at the top of your code
    - This can cause some tricky issues as the project grows

Application Factory
Instead of creating a Flask instance globally, you will create it inside a function
    - this function is known as the Application Factory
    - any configuration, registration and other setup the application needs will
    happen inside the function, then the application will be returned

__init__.py file serves double duty:
    - it will contain the application factory
    - it tells Python that the flaskr directory should be treated as a package

'''
