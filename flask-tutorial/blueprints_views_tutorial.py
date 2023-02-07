'''
Blueprints and Views

A view function is the code you write to respond to requests to your application
    - Flask uses patterns to match incoming requests URL to the view that should
    handle it
    - The view returns data that Flask turns into an outgoing response
    - Flask can also go the other direction and generate a URL to a view based
    on its name and arguments


Create a Blueprint

A blueprint is a way to organize a group of related views and other code
    - Rather than registering views and other code directly with an application
    they are registered with a blueprint
    - Then the blueprint is registered with the application when it is available
    in the factory function

Flaskr will have two blueprints, one for authentication functions and one for
the blog posts functions
    - The code for each blueprint will go in a seperate module
    - Since the blog needs to know about authentication you will write the
    authentication one first 

'''
