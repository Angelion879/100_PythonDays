# Question 10
# Write a program that accepts a sequence of whitespace separated
# words as input and prints the words after removing all duplicate
# words and sorting them alphanumerically.

def sort_string_alphanumerically(user_input):
    word_list = user_input.split(' ')
    word_list.sort()
    return ' '.join(word_list)


def pop_out_duplicate_words(user_input):
    word_list = user_input.split(' ')
    cleaned_word_list = list(dict.fromkeys(word_list))
    return ' '.join(cleaned_word_list)

# Question 11
# Write a program which accepts a sequence of comma separated 4 digit
# binary numbers as its input and then check whether they are divisible by 5 or not.

def divisible_by_five(user_input):
    value_list = user_input.split(',')
    final_list = []
    for i in range(len(value_list)):
        if int(value_list[i], 2) % 5 == 0:
            final_list.append(value_list[i])
    return ','.join(final_list)