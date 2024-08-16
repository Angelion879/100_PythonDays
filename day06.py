# Question 15
# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
def square_of_odd_numbers(user_input):
    input_digit_list = list(user_input.split(','))
    output_list = []

    for i in input_digit_list:
        if int(i)%2 != 0:
            output_list.append(str(int(i)**2))

    return ','.join(output_list)

# Question 16

