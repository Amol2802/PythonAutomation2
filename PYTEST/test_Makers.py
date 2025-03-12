import pytest

@pytest.mark.xfail
@pytest.mark.Sanity
def test_method1():
    print("this is method one test case")
    assert False

@pytest.mark.xfail
@pytest.mark.Regression
def test_method2():
    print("this is method 2 test case")
    assert True

@pytest.mark.xfail
@pytest.mark.Smoke
def test_method3():
    print("this is method 3 test case")
    assert False

@pytest.mark.xfail
@pytest.mark.Sanity
def test_method4():
    print("this is method 4 test case")
    assert True

@pytest.mark.xfail
@pytest.mark.Regression
def test_method5():
    print("this is method 2 test case")
    assert False