import pytest
from app import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True    
    with app.app.test_client() as client:
        yield client

def test_apollo_api(client):
    rv = client.get('/apollo')
    assert b'eagle has landed' in rv.data
