'''
Define and Access the Database

Python comes with built-in support for SQLite in the sqlite3 module

SQLite doesnt require setting up a separate database server and is build-in to
Python
    - Concurrent requests try to write to the db at the same time, they will
    slow down as each write happens sequentially
    - Small applications wont notice this but as it scales up switching to a
    different database is recommended

The first thing to do when working with a SQLite database (and most other python
database libraries) is to create a connection to it
    - Any queries and operations are performed using the connection which is
    which is closed after the work is finished

In web applications this connection is typically tied to the request.
    - It is created at some point when handling a request and closed before the
    response is sent 
'''
