def greet(name, greeting, punctuation = '.'):
    return f"{greeting.capitalize()}, {name.title()}{punctuation}"

print(greet("Antonina", "Hello")) # Hello, Antonina.
print(greet("Pete", "Good morning", "!")) # Good Morning, Pete!