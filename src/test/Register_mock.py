import unittest
from unittest.mock import patch
from src.user_logic.Register import Register
import os
import io
import sys


class TestRegister(unittest.TestCase):

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_register_success(self, mock_stdout, mock_input):
        mock_input.side_effect = ['studentID@student.com', 'Firstname', 'Lastname', '123456789']
        register_instance = Register("customer.csv")
        register_instance.register()
        self.assertIn("Signed up successfully!", mock_stdout.getvalue())

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_register_failure(self, mock_stdout, mock_input):
        mock_input.side_effect = ['Hello@world.com', 'Hello', 'World', 'Bye']
        with patch('os.path.exists') as mock_exists:
            mock_exists.return_value = False
            register_instance = Register("customer.csv")
            register_instance.register()
            self.assertIn("Resource directory does not exist.", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
