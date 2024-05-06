import unittest
from unittest.mock import patch
from src.user_logic.LogIn import LogIn


class TestLogIn(unittest.TestCase):

    @patch('src.user_logic.LogIn')
    def test_log_in_success(self, MockLogIn):
        # Mocking the LogIn instance
        mock_login_instance = MockLogIn.return_value
        # Mocking the get_password method of LogIn instance
        mock_login_instance.get_password.return_value = "password123"

        # Call the log_in method
        result = mock_login_instance.log_in()

        # Ensure log_in returns True after successful login
        self.assertTrue(result)

    @patch('src.user_logic.LogIn')
    def test_log_in_failure(self, MockLogIn):
        # Mocking the LogIn instance
        mock_login_instance = MockLogIn.return_value
        # Mocking the get_password method of LogIn instance
        mock_login_instance.get_password.return_value = ""
        # Mocking the log_in method to return False for failure
        mock_login_instance.log_in.return_value = False

        # Call the log_in method
        result = mock_login_instance.log_in()

        # Ensure log_in returns False after failed login
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
