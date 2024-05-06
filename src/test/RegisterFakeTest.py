import unittest
import io
from src.test.RegisterFake import RegisterFake
from unittest.mock import patch

class RegisterFakeTest(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_register_stub(self, mock_stdout):
        register_stub = RegisterFake()
        register_stub.register()

        printed_output = mock_stdout.getvalue().strip()

        self.assertIn("Signed up successfully!", printed_output)




