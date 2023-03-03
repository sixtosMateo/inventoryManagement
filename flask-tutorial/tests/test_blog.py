'''
- All the blog views use the auth fixture.
- Call auth.login() and subsequent requests from the client will be logged in as
the test user

The index view should display information about the post that was added with the
test data
    - When logged in as the author, there should be a link to edit the post

You can also test some more authentication behavior while testing the index view

When not logged in each page shows links to log in or register
When logged in theres a link to log out
'''

def test_index(client, auth):
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test on 2018-01-01' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data
