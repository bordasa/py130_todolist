def concatenate(*args):
    # full_string = ''

    # for arg in args:
    #     full_string += f"{arg} "
    
    # return full_string
    return " ".join(args)

print(concatenate("Launch", "School", "is", "great")) # Launch School is great
print(concatenate("I", "am", "working", "on", "the", "PY130", "course")) # I am working on the PY130 course