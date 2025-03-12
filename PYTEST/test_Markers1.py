import pytest

@pytest.mark.xfail
@pytest.mark.Sanity
@pytest.mark.Smoke
@pytest.mark.Regression
def test_method6():
    print("this is method 6 test case")
    assert True

@pytest.mark.xfail
@pytest.mark.Regression
def test_method7():
    print("this is method 7 test case")
    assert True

@pytest.mark.xfail
@pytest.mark.Smoke
def test_method8():
    print("this is method 8 test case")
    assert False

@pytest.mark.xfail
@pytest.mark.Sanity
def test_method9():
    print("this is method 9 test case")
    assert True