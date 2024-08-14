import unittest
from day04 import *

class DayFourExercises(unittest.TestCase):
    def test_string_sort(self):
        expected_result = 'again and hello makes perfect practice world'
        test_input = 'hello world and practice makes perfect again'
        actual_result = sort_string_alphanumerically(test_input)
        self.assertEqual(expected_result, actual_result)

    def test_popping_duplicates_out(self):
        expected_result = 'again and hello makes perfect practice world'
        test_input = 'again and and hello hello makes perfect practice world world'
        actual_result = pop_out_duplicate_words(test_input)
        self.assertEqual(expected_result, actual_result)

    def test_divisible_by_five(self):
        expected_result = '1010'
        test_input = '0100,0011,1010,1001'
        actual_result = divisible_by_five(test_input)
        self.assertEqual(expected_result, actual_result)

    def test_all_even_digits(self):
        expected_result = '2000,2002,2004,2006,2008'

        self.assertEqual(expected_result, get_only_all_even_digits_numbers())