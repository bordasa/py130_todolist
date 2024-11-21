# def concatenate(*strings):
#     new_string_list = []

#     for string in strings:
#         new_string_list.append(string)
    
#     return ' '.join(new_string_list)

def concatenate(*args):
    return ' '.join(args)

print(concatenate("Launch", "School", "is", "great")) # Launch School is great
print(concatenate("I", "am", "working", "on", "the", "PY130", "course")) # I am working on the PY130 course