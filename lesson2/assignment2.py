# Problem 1
# def combine(arg1, arg2, arg3):
#     return (arg1, arg2, arg3)

# print(combine(1, 2, 3))
# print(combine('aslk', 'oe', 'clad'))

# Problem 2
# def multiply(a, b, /):
#     return a * b

# print(multiply(3, 4))
# multiply(a=4, b=5)

# Problem 3
# def describe_pet(animal_type, *, name = ''):
#     if name:
#         print(f"{name} the {animal_type} is beautiful.")
#     else:
#         print(f"Your {animal_type} has no name?")

# describe_pet('dog')
# describe_pet('cat', name='Lola')

# Problem 4
# def calculate_average(*args):
#     if args:
#         return round((sum(args) / len(args)), 2)
#     else:
#         return None

# print(calculate_average(4, 3, 2, 1, 5, 6, 4, 5, 8, 9, 3, 7))
# print(calculate_average())

# Problem 5
def find_person(**kwargs):
    for name, profession in kwargs.items():
        if name == 'Antonina':
            return f"{name} has the profession of {profession}."
    
    return "Antonina not found"

print(find_person(John="Engineer", Antonina="Software Engineer"))
# Antonina's profession is Software Engineer

print(find_person(John="Engineer", Ginni="Software Engineer"))
# Antonina not found