import unittest
from day03 import *


class DayThreeExercises(unittest.TestCase):
    def test_matrix_generator_class(self):
        expected_result = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
        test_input = '3,5'
        test_matrix = MatrixGenerator(test_input)
        test_matrix.matrix_build()

        self.assertEqual(expected_result, test_matrix.matrix)

    def test_word_sorter(self):
        expected_result = 'bag,hello,without,world'
        test_input = 'without,hello,bag,world'
        actual_result = sort_by_initial_letter(test_input)

        self.assertEqual(expected_result, actual_result)
