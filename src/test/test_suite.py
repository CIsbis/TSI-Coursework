import unittest

from src.test.LogInStubTest import LogInStubTest
from src.test.LoginMock import LoginMock
from src.test.RegisterFakeTest import RegisterFakeTest
from src.test.RegisterMock import RegisterMock


def test_suite():
    suite = unittest.TestSuite()

    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(RegisterMock))
    suite.addTest(loader.loadTestsFromTestCase(LoginMock))
    suite.addTest(loader.loadTestsFromTestCase(LogInStubTest))
    suite.addTest(loader.loadTestsFromTestCase(RegisterFakeTest))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_suite())
