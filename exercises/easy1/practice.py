# Square Numbers

# numbers = [1, 2, 3, 4, 5]

# def square_it(num):
#     return num ** 2

# squared_nums = list(map(square_it, numbers))

# print(squared_nums)

# Problem 2: 

# only_even = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
# print(only_even)

# Problem 3: Product of Numbers
# from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# prod_of_all = reduce(lambda x, y: x * y, numbers)
# print(prod_of_all)

# Problem 4: Lengths of Strings
# def lengths(string):
#     return len(string)

# strings_list = ['adlfakj', 'a', '', 'safl']

# new_list = list(map(lengths, strings_list))
# new_list2 = list(map(lambda string: len(string), strings_list))
# new_list3 = list(map(len, strings_list))
# print(new_list)
# print(new_list2)
# print(new_list3)

# Problem 5: 
# random_list = ['alskfj', None, 0, '', 11]

# no_nones = list(filter(lambda x: x != None, random_list))
# print(no_nones)

# Problem 6:
# from functools import reduce

# l_of_strs = ['af', 'asf', 'asfasfd']

# new_str = reduce(lambda x, y: x + y, l_of_strs)

# print(new_str)

# Problem 7:
nested_list = [[1, 2], [3, 4, 5], [6], []]

flat_list = list((num
                    for sublist in nested_list
                    for num in sublist))

print(flat_list)