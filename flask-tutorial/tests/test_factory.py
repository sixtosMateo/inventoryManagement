from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

'''
The client argument in test_hello function,
represents the client fixture inside coftest.py.

This client argument calls the client fixuture function: 
'''
def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
