import unittest
from src.user_logic.Register import Register
from src.test.RegisterStub import RegisterStub
import io
import sys

class TestRegisterWithStub(unittest.TestCase):

    def test_register_success_with_stub(self):
        register_stub = RegisterStub()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        register_instance = Register(register_stub)
        register_instance.register()

        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue().strip()

        self.assertIn("Signed up successfully!", printed_output)


if __name__ == '__main__':
    unittest.main()
