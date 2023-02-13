'''
TEMPLATES
Templates are files that contain static data as well as placeholders for dynamic
data
    - a template is rendered with specific data to produce a final document
    - flask uses Jinja template library to render templates

In application, will use templates to render html which will display in the user
browser

In Flask, Jinja is configured to autoescape any data that is rendered in HTML
templates
    - this means that it's safe to render user input
        * any characters theyve entered that could mess with the html such as
        < and > will be escaped with safe values that look the same in the
        browser but dont cause unwanted effects

Jinja looks and behaves mostly like Python
    - Special delimeters are used to distiguish Jinja syntax from the static data
    in the template
    - Anything between {{ and }} is an expression that will be output to the
    final document
    - {% and %} denotes a control flow statement like if and for
    - unlike Python, blocks are denoted by start and end tags rather than
    indentation since static text within a block could change indentation


Base Layout:
Each page in the application will have the same basic layout around a different
body
    - instead of writing the entire HTML structure in each template, each template
    will extend a base template and override specific sections

'''
