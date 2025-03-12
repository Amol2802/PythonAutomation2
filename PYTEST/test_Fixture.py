import pytest

@pytest.fixture
def setup():
    print("this is setup method")
@pytest.fixture
def test_login(setup):
    print("this is login test")

def test_vrifyTitle(setup):
    print("this is verify title")

def test_vrifyHomePage(test_login):
    print("this is verify home page")
