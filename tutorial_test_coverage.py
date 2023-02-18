'''
Test Coverage:

Writing unit tests for your application lets you check that the code you wrote
works the way you expect
    - Flask provides a test client that simulates requests to the application
    and returns the response data

You should test as much of your code as possible.
    - Code in functions only runs when the function is called and code in branches
    such as if blocks, only runs when the condition is met
    - You want to make sure that each function is tested with data that covers
    each branch

The closer you get to 100% coverage, the more comfortable you can be that making
a change wont unexpectedly change other behavior
    - However 100% coverage doesnt guarantee that your application doesnt have
    bugs
    - In particular, it doesnt test how the user interacts with the application
    in the browser

Youll will user pytest and coverage to test and measure your code.
Install them both
'''

'''
Setup and Fixtures
The test code is located in the tests directory. This directory is next to the
flaskr package not inside it

Fixtures:
The tests/conftest.py file contains setup functions called fixtures that each test
will use
    - Tests are in Python modules that start with test_ and each test function in
    those modules also starts with test_

Each test will create a new temporary database file and populate some data that
will be used in the test

Write a SQL file to insert that data
    tests/data.sql
        INSERT INTO user (username, password)
        VALUES
        ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
        ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

        INSERT INTO post (title, body, author_id, created)
        VALUES
        ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');

This app fixture will call the factory and pass test_config to configure the
application and database for testing instead of using your local development
configuration

'''
