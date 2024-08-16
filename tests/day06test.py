import unittest
from day06 import *


class DaySixExercises(unittest.TestCase):

    def test_square_of_odd_numbers(self):
        expected_result = '1,9,25,49,81'
        test_input = '1,2,3,4,5,6,7,8,9'
        actual_result = square_of_odd_numbers(test_input)

        self.assertEqual(expected_result, actual_result)