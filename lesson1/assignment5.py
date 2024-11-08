def print_squares(numbers_list):
    for number in numbers_list:
        print(number**2)

print_squares([1, 2, 3, 4, 5])

def for_each(callback, iterable):
    for item in iterable:
        callback(item)

for_each(lambda number: print(number**2), [1, 2, 3, 4, 5])

pets = ('cat', 'dog', 'fish', 'bearded dragon')
for_each(lambda string: print(string.title()), pets)

nested_lists = [[1, 2], [3, 4], [5, 6, 7]]
for_each(lambda sublist: sublist.pop(), nested_lists)
print(nested_lists)

def times(callback, count):
    for item in range(count):
        callback(item)

times(lambda number: print(number**2), 5)
# 0
# 1
# 4
# 9
# 16

pets = ('cat', 'dog', 'fish', 'bearded dragon')
new_pets = []
times(lambda index: new_pets.append(pets[index].title()),
      len(pets))
print(new_pets)
# ['Cat', 'Dog', 'Fish', 'Bearded Dragon']
