import math


# Question 4
# Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number
def generate_list_and_tuple(string_input):
    format_to_list = string_input.split(',')
    format_to_tuple = tuple(format_to_list)
    return f"{format_to_list}\n{format_to_tuple}"


# Question 5
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
class StringHandler:

    def __init__(self):
        self.inputString = ''

    def get_string(self, user_input):
        self.inputString = user_input.upper()

    def print_string(self):
        print(self.inputString)


# Question 3
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence
class FormulaCalculator:
    result_list = []

    def __init__(self, user_input):
        self.values = user_input.split(',')
        self.iterations = len(self.values)

    def apply_formula(self, value):
        integer_result = int(math.sqrt((2 * 50 * value) / 30))
        return integer_result

    def result_builder(self):
        for i in range(0, self.iterations):
            integer_value = int(self.values[i])
            self.result_list.append(self.apply_formula(integer_value))

        return self.result_list
