import pytest, sys, random, py, pytest, os
from xprocess import ProcessStarter
from lib.database_connection import DatabaseConnection
from app import app

# This is a Pytest fixture.
# It creates an object that we can use in our tests.
# We will use it to create a database connection.
@pytest.fixture
def db_connection():
    conn = DatabaseConnection(test_mode=True)
    conn.connect()
    return conn

# We'll also create a fixture for the client we'll use to make test requests.
@pytest.fixture
def web_client():
    app.config['TESTING'] = True # This gets us better errors
    with app.test_client() as client:
        yield client


# @pytest.fixture
# def test_web_address(xprocess):
#     python_executable = sys.executable
#     app_file = py.path.local(__file__).dirpath("../app.py")
#     port = str(random.randint(4000, 4099))
#     class Starter(ProcessStarter):
#         env = {"PORT": port.}
# Now, when we create a test, if we allow it to accept a parameter called
# `db_connection` or `web_client`, Pytest will automatically pass in the objects
# we created above.

# For example:

# def test_something(db_connection, web_client):
#     # db_connection is now available to us in this test.
#     # web_client is now available to us in this test
