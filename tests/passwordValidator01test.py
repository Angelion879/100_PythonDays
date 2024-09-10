import unittest
from passwordValidator01 import password_validator


class ValidatorTest(unittest.TestCase):

    def test_valid_password_input(self):
        expected_result = 'Accepted'
        test_input = 'P@ssword101%'
        actual_result = password_validator(test_input)

        self.assertEqual(expected_result, actual_result)

    def test_short_password(self):
        expected_result = 'Unaccepted'
        test_input = 'W0rd$'
        actual_result = password_validator(test_input)

        self.assertEqual(expected_result, actual_result)

    def test_no_specialcharacter_password(self):
        expected_result = 'Unaccepted'
        test_input = 'Password101'
        actual_result = password_validator(test_input)

        self.assertEqual(expected_result, actual_result)

    def test_no_number_password(self):
        expected_result = 'Unaccepted'
        test_input = 'P@sswords'
        actual_result = password_validator(test_input)

        self.assertEqual(expected_result, actual_result)

    def test_no_uppercase_password(self):
        expected_result = 'Unaccepted'
        test_input = 'p@ssword101'
        actual_result = password_validator(test_input)

        self.assertEqual(expected_result, actual_result)

    def test_no_lowercase_password(self):
        expected_result = 'Unaccepted'
        test_input = 'P@SSWORD101'
        actual_result = password_validator(test_input)

        self.assertEqual(expected_result, actual_result)
