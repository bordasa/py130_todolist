# lst = [4, 2, 5, 6, 3, None, 23, 5]

# new_list = list(filter(lambda item: item is not None, lst))

# print(new_list)

# nested_list = [[1, 2, 3], [4, 5], [6]]

# flat_list = list((num 
#                     for sublist in nested_list
#                     for num in sublist))

# # for num in nested_generator:
#     # print(num)
# print(flat_list)

def user_input_generator():
    while True:
        user_input = input("Type anything except 'stop':\n")

        if user_input.lower() == 'stop':
            break

        yield user_input

for user_input in user_input_generator():
    print(user_input)