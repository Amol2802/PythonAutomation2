import pytest

@pytest.fixture()
#@pytest.yield_fixture()  # deprecated
def setup():
    print("this is setup method")
    yield
    print("this code will execute after test case")

def test_login(setup):
    print("this is login test")

def test_vrifyTitle(setup):
    print("this is verify title")

