from app import app 


def test_app(): 
    assert app() == 'Hello, Python!'
