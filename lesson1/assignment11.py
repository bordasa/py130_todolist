file = open('example.txt', 'r')
content = file.read()
file.close()

print(repr(content))

file = open('example.txt', 'w')
file.write('Testing 1, 2, 3.\n')
file.close()

with open('example.txt', 'r') as file:
    for line in file:
        print(line)

with open('example.txt', 'w') as file:
    file.write('Running dog\nSleeping cat\nSwimm fish\nSinging bird\n')

with open('example.txt', 'a') as file:
    file.write('Mooing cow')

with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))
