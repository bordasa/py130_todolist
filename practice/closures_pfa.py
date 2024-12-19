# # # def add(x, y):
# # #     return x + y

# # # def make_adder(x):
# # #     def adder(y):
# # #         return add(x, y)
    
# # #     return adder

# # # plus5 = make_adder(5)

# # # print(plus5(10))
# # from functools import partial

# # def add(x, y):
# #     return x + y

# # adders = [partial(add, x) for x in range(1, 4)]

# # add1, add2, add3 = adders

# # print(add1(10))
# # print(add2(10))
# # print(add3(10))

# def later(func, argument):
#     def new_func():
#         return func(argument)

#     return new_func

# def printer(message):
#     print(message)

# print_warning = later(printer, "The system is shutting down!")
# print_warning()  # The system is shutting down!

def later2(func, first_arg):
    def inner(second_arg):
        return func(first_arg, second_arg)
    return inner

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!