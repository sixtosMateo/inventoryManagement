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
The test code is located in the tests directory. 
'''
