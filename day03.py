# Question 7
# Write a program which takes 2 digits, X,Y as input and generates a
# 2-dimensional array. The element value in the i-th row and j-th
# column of the array should be i _ j.*
class MatrixGenerator:
    def __init__(self, user_input):
        self.matrix = []
        self.row_amount, self.column_amount = map(int, user_input.split(','))

    def matrix_build(self):
        for i in range(self.row_amount):
            temporary_row = self.row_build(i)
            self.matrix.append(temporary_row)

    def row_build(self, current_row):
        row = []
        for j in range(self.column_amount):
            row.append(current_row * j)
        return row


# Question 8

def sort_by_initial_letter(user_input):
    word_list = user_input.split(',')
    word_list.sort()
    return ','.join(word_list)
