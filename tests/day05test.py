import unittest
from day05 import *


class DayFiveExercises(unittest.TestCase):

    def test_letters_or_numbers(self):
        expected_result = 'LETTERS 10\nDIGITS 3'
        test_input = 'hello world! 123'
        actual_result = letters_or_numbers(test_input)

        self.assertEqual(expected_result, actual_result)

    def test_upper_or_lower_case(self):
        expected_result = 'UPPER CASE 2\nLOWER CASE 8'
        test_input = 'Hello World!'
        actual_result = upper_or_lower_case(test_input)

        self.assertEqual(expected_result, actual_result)