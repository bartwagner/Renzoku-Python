word = 'Hello'
name = 'World'
sentence = word + ' ' + name
print(sentence)
print('----------------')

word = 'Goodbye'
print(sentence)
print('----------------')

for character in name:
    print(character)
print('----------------')

for character in name:
    print(character)
    print('---')
print('----------------')

for character in name:
    print('---' + character)
print('----------------')

name = 'Amy'
for character in name:
    print(name)
print('----------------')

name = 'World'
for character in name:
    print(name)
print('----------------')

hello = 'Hello'
print(hello)
hello = hello + '!'
print(hello)
print('----------------')

temp = hello + '!'
hello = temp

name = 'World'
line = '-'
for char in name:
    line = line + char
    print(line)
print('----------------')

name = 'World'
line = ''
for char in name:
    line += char
    print(name)
print('----------------')

name = 'World'
line = ''
colunm = '|'
plus = '+'
for _ in name:
    line += '-'
name = colunm + name + colunm
line = plus + line + plus
print(line)
print(name)
print(line)
print('----------------')

name = 'World'
line = '+' + name + '+'
spaces = ''
for _ in name:
    spaces += ' '

print(line)
for char in name:
    print(char + spaces + char)
print(line)
print('----------------')

name = 'World'
space = ''
for char in name:
    print(space + char)
    space += ' '
print('----------------')