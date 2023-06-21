words = ['This','is','a','list']
for word in words:
    print(word)
print('----------------')

x = 1
things = ['Hello', x, x + 3]
print(things)
print('----------------')

numbers = [3, 1, 4, 1, 5, 9]
total = 0
for number in numbers:
    total += number
print(total)
print('----------------')

words = ['This', 'is', 'a', 'list']
totalsum = ''
for word in words:
    totalsum += word
print(totalsum)
print('----------------')

words = ['This', 'is', 'a', 'list']
separator = ' - '
totalsum = ''
not_first = False
for word in words:
    if not_first:
        totalsum += separator
    totalsum += word
    not_first = True
print(totalsum)
print('----------------')

numbers = [1, 2] + [3, 4]
print(numbers)
new_numbers = []
new_numbers += numbers
new_numbers += [5]
print(new_numbers)
print('----------------')

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
new_numbers = []
for number in numbers:
    new_numbers += [number * 2]
print(new_numbers)
print('----------------')

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
new_numbers = []
for number in numbers:
    if number > 5:
        new_numbers.append(number)
print(new_numbers)
print('----------------')

things = ['This', 'is', 'a', 'list']
thing_to_find = 'is'
found = False
for thing in things:
    if thing == thing_to_find:
        found = True
        break
print(found)
print('----------------')

words = ['This', 'is', 'a', 'list']
print(words[0])
print(words[1])
print(words[2])
print(words[3])
print('----------------')

words = ['This', 'is', 'a', 'list']
indices = range(4)
for index in indices:
    print(index)
    print(words[index])
print('----------------')

indices = range(4)
print(indices[0])
print(indices[1])
print(indices[2])
print(indices[3])
print('----------------')

words = ['This', 'is', 'a', 'list']
print(len(words))
print('----------------')

words = ['This', 'is', 'a', 'list']
print(words[3])
print('----------------')

words = ['Python']
print(words[len(words)-1])
print('----------------')

words = ['Python', 'Hello']
for index in range(len(words)):
    print(index)
    print(words[index])
print('----------------')

things = ['on', 'the', 'way', 'to', 'the', 'store']
to_find = 'the'
for index in range(len(things)):
    if things[index] == to_find:
        print(index)
        break
print('----------------')

