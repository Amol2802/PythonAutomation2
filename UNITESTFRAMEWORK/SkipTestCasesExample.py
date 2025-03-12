import unittest


class  LoginApp(unittest.TestCase):

    def testTestcase1(self):
        print("This is Testcase 1")

    @unittest.SkipTest
    def testTestcase2(self):
        print("This is Testcase 2")

    @unittest.skip("I am skipping the test case because it sin not part of the regression  test case 3")
    def testTestcase3(self):
        print("This is Testcase 3")

    def testTestcase4(self):
        print("This is Testcase 4")

    @unittest.skipIf(3==3,"the given numbers are equals test case 5")
    def testTestcase5(self):
        print("This is Testcase 5")

if __name__ == "__main__":
    unittest.main()