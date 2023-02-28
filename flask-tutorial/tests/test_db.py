import sqlite3

import pytest
from flaskr.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        ''' within the application context
        get_db should return the same connection each time it us called
        '''
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)

'''
The init-db command that was initialize in the db.py file should call the
init_db function(found in db.py file) and output message

'''
def test_init_db_command(runner, monkeypatch):

    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True
    '''
    This test uses Pytest's Monkeypatch fixture to replace the init_db function
    with one that records that it's been called.

    The runner fixture you wrote(conftest.py) is used to call the init-db command
    '''
    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
