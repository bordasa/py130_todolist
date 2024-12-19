def combine(x, y, z):
    return (x, y, z)

def multiply(x, y, /):
    return x * y

def describe_pet(animal_type, *, name = ''):
    print(f"Your {animal_type} has the name {name}.")

def calculate_average(*args):
    if args:
        return sum(args) / len(args)
    return None

def find_person(*kwargs):
    if "Antonina" in kwargs:
        print(f"Antonina's profession is: {kwargs["Antonina"]}.")
    print("Antonina not found.")

def concat_strings(*args, sep=' '):
    return sep.join(args)

def register(username, /, age = None, *, password):
    pass

def print_message(*, message, level='INFO'):
    print(f"[{level}] {message}")