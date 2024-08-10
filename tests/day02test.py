import unittest
from unittest.mock import patch
import sys
import io
from day02 import *


class DayTwoExercises(unittest.TestCase):
    def test_list_and_tuple_generator(self):
        test_input = "34,67,55,33,12,98"
        expected_result = "['34', '67', '55', '33', '12', '98']\n('34', '67', '55', '33', '12', '98')"

        self.assertEqual(expected_result, generate_list_and_tuple(test_input))

    def test_upper_case_class_input(self):
        expected_result = 'HELLO WORLD'
        test_input = 'hello world'
        test_string = StringHandler()
        test_string.get_string(test_input)

        self.assertEqual(test_string.inputString, expected_result)

    def test_upper_case_class_output(self):
        expected_result = 'HELLO WORLD\n'
        test_input = 'hello world'

        test_string = StringHandler()
        test_string.get_string(test_input)

        with patch('sys.stdout', new=io.StringIO()) as capture_output:
            test_string.print_string()
            self.assertEqual(capture_output.getvalue(), expected_result)

    def test_formulae_calculator(self):
        expected_result = [18, 22, 24]
        test_calculator = FormulaCalculator('100,150,180')
        actual_result = test_calculator.result_builder()

        self.assertEqual(actual_result, expected_result)