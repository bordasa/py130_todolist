def display_info(data, /, *, reverse = False, uppercase = False):
    string = data

    if reverse:
        string = string[::-1]
    
    if uppercase:
        string.upper()
    
    return string

print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC