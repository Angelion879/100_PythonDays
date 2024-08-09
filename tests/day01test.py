import unittest
from day01 import *


class DayOneExercises(unittest.TestCase):
    def test_divisible_by_seven_but_not_by_five(self):
        expected_result = [7, 14, 21, 28, 42, 49]

        self.assertEqual(expected_result, divisible_by_seven())

    def test_factorial_number_calculator(self):
        test_input = 8
        expected_value = 40320

        self.assertEqual(expected_value, factorial_of_number(test_input))

    def test_square_number_dictionary_generator(self):
        test_input = 10
        expected_result = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

        self.assertEqual(expected_result, generator_of_squares(test_input))
