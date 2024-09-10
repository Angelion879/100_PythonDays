import unittest
from passwordValidator01 import password_validator


class ValidatorTest(unittest.TestCase):

    def test_valid_password_input(self):
        expected_result = 'Accepted'
        test_input = 'password1'
        actual_result = password_validator(test_input)

        self.assertEqual(expected_result, actual_result)

    def test_invalid_password_input(self):
        expected_result = 'Unaccepted'
        test_input = 'word'
        actual_result = password_validator(test_input)

        self.assertEqual(expected_result, actual_result)
