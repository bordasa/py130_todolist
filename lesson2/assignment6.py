# Problem 4

def later(func, argument):

    def new_func():
        return func(argument)

    return new_func

def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()  # The system is shutting down!

# Problem 5

def later2(func, first_arg):

    def inner(second_arg):
        return func(first_arg, second_arg)

    return inner

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!