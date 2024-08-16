# Question  13
# Write a program that accepts a sentence and calculate the number of letters and digits.
def letters_or_numbers(user_input):
    character_list = list(user_input)
    number_counter = 0
    letter_counter = 0

    for i in character_list:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            letter_counter += 1
        elif '0' <= i <= '9':
            number_counter += 1

    return f'LETTERS {letter_counter}\nDIGITS {number_counter}'


# Question 14
# Write a program that accepts a sentence and calculate the number
# of upper case letters and lower case letters.
def upper_or_lower_case(user_input):
    character_list = list(user_input)
    upper_counter = 0
    lower_counter = 0

    for i in character_list:
        if 'a' <= i <= 'z':
            lower_counter += 1
        elif 'A' <= i <= 'Z':
            upper_counter += 1

    return f'UPPER CASE {upper_counter}\nLOWER CASE {lower_counter}'
