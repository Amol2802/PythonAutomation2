import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

def setUpModule():
    print("This is setUp Moldule Method @@@@@@@@@@@@@@@")

def tearDownModule():
    print("This is tearDown Moldule Method@@@@@@@@@@@@")

class  AppliactionTesting(unittest.TestCase):

    @classmethod      # decoratore or anotation
    def setUp(self):
        print("this is login Appliction code")

    @classmethod
    def tearDown(self):
        print("this is logout Appliction code")

    @classmethod
    def setUpClass(cls):
        print("this is SetUp Class Method*&&&&&&&&&&&&&&&&&&&&&&&&&&")

    @classmethod
    def tearDownClass(cls):
        print("this is tearDown Class Method*&&&&&&&&&&&&&&&&&&&&&&&&&&")

    def test_Method1(self):
        print("This is TestCase**************1")

    def test_Method2(self):
        print("This is TestCase**************2")

    def test_Method3(self):
        print("This is TestCase**************3")

    def test_Method4(self):
        print("This is TestCase**************4")


if __name__== "__main__":
    unittest.main()
