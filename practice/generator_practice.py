#Question 1
# reciprocals = (1/n for n in range(1, 11))
# for val in reciprocals:
#     print(val)

# def reciprocals(n):
#     for number in range(1, n + 1):
#         yield 1 / number

# for value in reciprocals(7):
#     print(value)
# list_of_strings = ['asfk', 'alkffkasdf', 'zlkj', 'kfdjsl']
# print(tuple(string.capitalize() for string in list_of_strings))

# def capitalize(strings):
#     for string in strings:
#         yield string.capitalize()

list_of_strings = ['four', 'score', 'and', 'seven', 'years', 'ago']
# print(tuple(capitalize(list_of_strings)))

# capitalize_long = (string.capitalize() for string in list_of_strings
#                    if len(string) >= 5)
# print(set(capitalize_long))

def capitalize_short(strings):
    for string in strings:
        if len(string) < 5:
            yield string.capitalize()

cap_long = capitalize_short(list_of_strings)
print(set(cap_long))