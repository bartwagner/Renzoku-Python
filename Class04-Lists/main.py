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

string1 = 'Hello'
string2 = 'World'
for index in range(len(string1)):
    print(string1[index], string2[index])
print('----------------')

string1 = 'Hello'
string2 = 'World'
for i in range(len(string1)):
    char1 = string1[i]
    char2 = string2[i]
    print(char1 + ' ' + char2)
print('----------------')

string1 = 'Goodbye'
string2 = 'World'
lenght1 = len(string1)
lenght2 = len(string2)
if lenght1 > lenght2:
    value = lenght1
else:
    value = lenght2
for i in range(value):
    if i < lenght1:
        char1 = string1[i]
    else:
        char1 = ' '
    if i < lenght2:
        char2 = string2[i]
    else:
        char2 = ' '
    print(char1 + ' ' + char2)
print('----------------')

print(len)
print(print)
print(callable(len))
print('----------------')

f = 'a string'
print(callable(f))
#f() --doesn't work
print('----------------')

things = [1,2,3]
length = len(things)
printed = print(length)
print(printed)
print('----------------')

things = print([1,2,3])
#length = len(things) --doesn't work
print('----------------')

word = 'Hello'
print(word.upper)
print(word.upper())
print('----------------')

word = 'Hello'
#word.append('!') --doesn't work
print('----------------')

nums = [1, 2, 3]
new_nums = nums + [4, 5]
print(new_nums)
print(nums)
nums.append(4)
print(nums)
print('----------------')

nums = [1, 2, 3]
nums[1] = 9
print(nums)
print('----------------')

print([7, 8, 9, 8].index(7))
print([7, 8, 9, 8].index(8))
print([7, 8, 9, 8].index(9))
print('----------------')

nums = [1,2,3]
print(nums.pop(1))
print(nums)
print('----------------')

nums = [1,2,3]
nums.remove(1)
print(nums)
print('----------------')

x = ['a', 'b', 'c']
x.append(x.pop(0))
print(x)
print('----------------')

x = ['a', 'b', 'c']
x[len(x) - 1] = x[0]
print(x)
print('----------------')

x = ['a', 'b', 'c']
y = x + [x[0]]
print(y)
print('----------------')

x = [1, 2, 0, 3]
x.remove(0)
print(x)
print('----------------')

x = [1, 2, 0, 3]
x.pop(x.index(0))
print(x)
print('----------------')


print('----------------')