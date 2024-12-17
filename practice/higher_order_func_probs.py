# # def select(callback, iterable):
# #     result = []
# #     for el in iterable:
# #         if callback(el):
# #             result.append(el)
# #     return result
# def select(callback, iterable):
#     return [el for el in iterable if callback(el)]

# numbers = [1, 2, 3, 4, 5]
# colors = {'red', 'orange', 'yellow', 'green',
#           'blue', 'indigo', 'violet'}

# odd_numbers = select(lambda number: number % 2 != 0, numbers)
# print(odd_numbers)            # [1, 3, 5]

# large_numbers = select(lambda number: number >= 10, numbers)
# print(large_numbers)          # []

# small_numbers = select(lambda number: number < 10, numbers)
# print(small_numbers)          # [1, 2, 3, 4, 5]

# short_color_names = select(lambda color: len(color) <= 5, colors)
# print(short_color_names)      # ['blue', 'red', 'green']
# # The order of the colors may vary, but should include the
# # indicated colors.

# def reject(callback, iterable):
#     rejected = []
#     for el in iterable:
#         if not callback(el):
#             rejected.append(el)
#     return rejected

# def reject(callback, iterable):
#     return [item for item in iterable if not callback(item)]

# numbers = [1, 2, 3, 4, 5]
# colors = {'red', 'orange', 'yellow', 'green',
#           'blue', 'indigo', 'violet'}

# even_numbers = reject(lambda number: number % 2 != 0, numbers)
# print(even_numbers)            # [2, 4]

# small_numbers = reject(lambda number: number >= 10, numbers)
# print(small_numbers)          # [1, 2, 3, 4, 5]

# large_numbers = reject(lambda number: number < 10, numbers)
# print(large_numbers)          # []

# long_color_names = reject(lambda color: len(color) <= 5, colors)
# print(long_color_names)
# # ['yellow', 'violet', 'orange', 'indigo']
# # The order of the colors may vary, but should include the
# # indicated colors.

# def reduce(callback, iterable, accum):
#     for num in iterable:
#         accum = callback(num, accum)
#     return accum

# numbers = (1, 2, 4, 8, 16)
# total = lambda number, accum: accum + number
# print(reduce(total, numbers, 0))        # 31

# numbers = [10, 3, 5]
# product = lambda number, accum: accum * number
# print(reduce(product, numbers, 2))      # 300

# colors = ['red', 'orange', 'yellow', 'green',
#           'blue', 'indigo', 'violet']
# rainbow = lambda color, accum: accum + color[0].upper()
# print(reduce(rainbow, colors, ''))      # ROYGBIV

# def sum_of_squares(lst):
#     return reduce(lambda num, accum: num**2 + accum, lst, 0)

# print(sum_of_squares([3,7,2,9,5]))
