import unittest
from unittest.mock import patch
from src.user_logic.LogIn import LogIn

class LoginMock(unittest.TestCase):

    @patch('src.user_logic.LogIn')
    def test_log_in_success(self, MockLogIn):
        mock_login_instance = MockLogIn.return_value
        mock_login_instance.get_password.return_value = "password123"
        result = mock_login_instance.log_in()
        self.assertTrue(result)

    @patch('src.user_logic.LogIn')
    def test_log_in_failure(self, MockLogIn):
        mock_login_instance = MockLogIn.return_value
        mock_login_instance.get_password.return_value = ""
        mock_login_instance.log_in.return_value = False
        result = mock_login_instance.log_in()
        self.assertFalse(result)



