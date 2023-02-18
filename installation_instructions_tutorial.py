'''
Make the Project Installable:
Making your application installable means that you can build a distribution
file and install that in another environment
    - just like you installed Flask in your environment

This makes deploying your project the same as installing any other library
so you are using all the standard Python tools to manage everything

Other Benefits that come from having projects installable:
    - Currently, Python and Flask understand how to use the flaskr package
    only because youre running from your project directory
        * Installing means you can import it no matter where you run from

    - You can manage your project's dependencies just like other packages do
    so pip install youproject.whl installs them

    - Test tools can isolate your test environment from your development
    environment
'''

'''
Describe the Project:
The setup.py file describes your project and the files that belong to it

setup.py
from setuptools import find_packages, setup

setup(
    name='flaskr'
    version='1.0.0'
    packages=find_packages()
    include_package_data=True
    install_requires='flask'
)

packages: tells Python what package directories (and the python files they
        contain) to include

find_packages(): find these directories automatically so you dont have to type
                them out. To include other files, such as the static and
                templates directories

include_package_data: is a set

Python needs another file named MANIFEST.in to tell what this other data is

    include flaskr/schema.sql
    graft flaskr/static
    graft flaskr/templates
    global -exclude *pyc

This tells Python to copy everything in the static and templates directories
and the schema.sql file, but to exclude all bytecode files

'''

'''
Install the Project:
Use pip to install your project in the virtual environment

    $ pip install -e .

This tells pip to find setup.py in the current directory and install it in
editable or developement mode
    - editable mode means that as you make changes to your local code, youll
    only need to re-install if you change the metadata about the project such
    as dependencies

You can observe that the poject is now installed with pip list

complete full Packaging tutorial and a detailed guide:
https://packaging.python.org/en/latest/tutorials/packaging-projects/
https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

'''
