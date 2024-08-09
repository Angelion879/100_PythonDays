# Question 1
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence
# on a single line.
def divisible_by_seven_not_by_five():
    numbers_divisible_by_seven_but_not_by_five = []
    for i in range(2000, 3200, +1):
        if (i % 7 == 0) and (i % 5 != 0):
            numbers_divisible_by_seven_but_not_by_five.append(i)
    return numbers_divisible_by_seven_but_not_by_five


# Question 2
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line
def factorial_of_number(number):
    final_factorial = 1
    for i in range(number, 1, -1):
        final_factorial *= i
    return final_factorial


# Question 3
# With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary
def generator_of_squares(number):
    square_numbers = dict()
    for i in range(1, number + 1, +1):
        square_numbers[i] = i * i
    return square_numbers
