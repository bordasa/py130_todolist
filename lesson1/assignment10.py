# # # reciprocals = (1/num for num in range(1,11))

# # # for recip in reciprocals:
# # #     print(recip)

# # # def reciprocals(n):
# # #     num = 1

# # #     while num <= n:
# # #         yield 1/num
# # #         num += 1

# # # for value in reciprocals(5):
# # #     print(value)

# list_of_strings = ['asf', 'asdf', 'asdf', 'asf', 'sdfadf', 'asdfaslfkj']

# # print(tuple(string.capitalize() for string in list_of_strings))

# capitalized = (string.capitalize() for string in list_of_strings
#                if len(string) >= 5)

# print(set(capitalized))

strings = ['four', 'score', 'and', 'seven', 'years', 'ago']

def capitalized(list_of_strings):
    for string in list_of_strings:
        if len(string) < 5:
            yield string.capitalize()

print(set(capitalized(strings)))