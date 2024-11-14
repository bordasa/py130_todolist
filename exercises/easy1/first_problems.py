# # Problem 1
# my_list = [1, 2, 3, 4, 5]

# squared_list = list(map(lambda x: x * x, my_list))
# print(squared_list)

# # Problem 2
# evens_only = list(filter(lambda x: x % 2 == 0, squared_list))
# print(evens_only)

# # Problem 3

# from functools import reduce

# product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
# print(product)

# # Problem 4
# list_of_strings = ['afds', 'fasdfas', 'asfdsdaf', 'asfd', 'd', '']
# # str_lengths = list(map(lambda string: len(string), list_of_strings))
# str_lengths = list(map(len, list_of_strings))
# print(str_lengths)

# Problem 5
# new_list = list(filter(bool, [None, 1, 2, 3, None, 3, 4, 5, None]))
# new_list = list(filter(lambda x: x is not None, ['', 1, False, None, 2, None, 3]))
# print(new_list)

# Problem 6
# from functools import reduce

# concat_strs = reduce(lambda x, y: x + y, ['asldfk', 'asldfkj', 'lkafj'])
# print(concat_strs)

# Problem 7
# nested_lists = [[1, 2, 3], [4, 5], [6]]

# flat_list = list((num
#                   for sublist in nested_lists
#                   for num in sublist))

# print(flat_list)

# Problem 8
# my_string = "Launch School"

# backwards_string = list(char for char in my_string[::-1])
# print(backwards_string)

string = "Hello"
# reverse_generator = (char for char in string[::-1])
# reverse_generator = (string[i] for i in range(len(string) - 1, -1, -1))

# for char in reverse_generator:
#     print(char)

# Problem 9
# def generator_func():
#     num = 1
#     while num < 6:
#         yield num
#         num += 1

# def number_generator():
#     for num in range(1, 6):
#         yield num

# # for number in generator_func():
# #     print(number)

# for number in number_generator():
#     print(number)

# Problem 10
def ask_until_stop():
    user_input = ''

    while user_input.lower() != 'stop':
        user_input = input('Type something: ')
        yield user_input
    
    yield 'Thank you'

for user_input in ask_until_stop():
    print(user_input)