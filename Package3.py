import unittest

from Package2.TCLogin1Package2 import loginFourth
from Package2.TCLoginPackage2 import loginThird
from Packege1 import TCLogin
from Packege1 import TCLogin2

from Package2 import TCLoginPackage2
from Package2 import TCLogin1Package2
from Packege1.TCLogin import loginFiirst
from Packege1.TCLogin2 import loginSecond

test1=unittest.TestLoader().loadTestsFromTestCase(loginFiirst)
test2=unittest.TestLoader().loadTestsFromTestCase(loginSecond)

test3=unittest.TestLoader().loadTestsFromTestCase(loginThird)
test4=unittest.TestLoader().loadTestsFromTestCase(loginFourth)

grp1=unittest.TestSuite([test1, test2])
grp2=unittest.TestSuite([test1, test2])

regression=unittest.TestSuite([test1, test2, test3, test4])

smoke=unittest.TestSuite([test1, test4, test3])

sanity=unittest.TestSuite([test2])

unittest.TextTestRunner().run(smoke)