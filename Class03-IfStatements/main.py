condition = True
print(condition)
condition = False
print(condition)
if not condition:
    print('This does not')
if condition:
    print('This gets printed')
print('----------------')

sentence = 'Hello World'
excited = True
if excited:
    sentence += '!'
print(sentence)
print('----------------')

sentence = 'Hello World'
excited = False
if excited:
    sentence += '!'
print(sentence)
print('----------------')

sentence = 'Hello'
excited = True
confused = True
if excited:
    sentence += '!'
if confused:
    sentence += '?'
print(sentence)
print('----------------')

sentence = 'Hello World'
excited = True
if excited:
    new_sentence = ''
    for char in sentence:
        new_sentence += char + '!'
    sentence = new_sentence
print(sentence)
print('----------------')

sentence = 'Hello World'
include = False
new_sentence = ''
for char in sentence:
    if include:
        new_sentence += char
    include = True
print(new_sentence)
print('----------------')

sentence = 'Hello World'
include = False
new_sentence = ''
for char in sentence:
    if include:
        new_sentence += char
    include = True
print(new_sentence)
print('----------------')

sentence = 'Hello there'
include = True
new_sentence = ''
for char in sentence:
    if include:
        new_sentence += char
    include = False
print(new_sentence)
print('----------------')

condition = True
if condition:
    print('Yes')
else:
    print('No')
print('----------------')

condition = False
if condition:
    print('Yes')
else:
    print('No')
print('----------------')

sentence = 'Hello World'
excited = True
if excited:
    sentence = sentence.upper()
else:
    sentence = sentence.lower()
print(sentence)
print('----------------')

sentence = 'Hello World'
excited = False
if excited:
    sentence = sentence.upper()
else:
    sentence = sentence.lower()
print(sentence)
print('----------------')

sentence = 'Hello World'
excited = True
if excited:
    char = '!'
sentence += char
print(sentence)
print('----------------')

sentence = 'Hello World'
excited = False
if excited:
    char = '!'
sentence += char
print(sentence)
print('----------------')

sentence = 'Hello there'
excited = False
if excited:
    char = '!'
    sentence += char
else:
    char = '.'
    sentence += char
print(sentence)
print('----------------')

sentence = 'HELLO THERE'
upper = True
new_sentence = ''
for char in sentence:
    if upper:
        char = char.upper()
    else:
        char = char.lower()
    new_sentence += char
    upper = False
print(new_sentence)
print('----------------')

sentence = 'One more exercise, and then you can relax'
upper = True
new_sentence = ''

for char in sentence:
    if upper:
        char = char.upper()
        upper = False
    else:
        char = char.lower()
        upper = True
    new_sentence += char
print(new_sentence)
print('----------------')

print(1 + 2 == 3)
print(4 + 5 == 6)
print('ab' + 'c' == 'a' + 'bc')
print('----------------')

name = 'kesha'
new_name = ''
for c in name:
    if c == 's':
        c = '$'
    new_name += c
print(new_name)
print('----------------')

name = 'kesha'
new_name = ''
for c in name:
    if c == 's':
        c = '$'
    if c == 'e':
        c = '3'
    if c == 'a':
        c = '@'
    new_name += c
print(new_name)
print('----------------')

dna = 'AGTAGCGTC'
opposite_dna = ''
for char in dna:
    if char == 'A':
        char = 'T'
    if char == 'T':
        char = 'A'
    if char == 'G':
        char = 'C'
    if char == 'C':
        char = 'G'
    opposite_dna += char
print(opposite_dna)
print('----------------')

dna = 'AGTAGCGTC'
opposite_dna = ''
for char in dna:
    if char == 'A':
        char = 'T'
    else:
        if char == 'T':
            char = 'A'
    if char == 'G':
        char = 'C'
    else:
        if char == 'C':
            char = 'G'
    opposite_dna += char
print(opposite_dna)
print('----------------')

dna = 'AGTAGCGTC'
opposite_dna = ''
for char in dna:
    if char == 'A':
        char = 'T'
    elif char == 'T':
          char = 'A'
    elif char == 'G':
          char = 'C'
    elif char == 'C':
          char = 'G'
    opposite_dna += char
print(opposite_dna)
print('----------------')

dna = 'AGTAGCGTC'
opposite_dna = ''
for char in dna:
    if char == 'A':
        char = 'T'
    elif char == 'T':
          char = 'A'
    elif char == 'G':
          char = 'C'
    else:
          char = 'G'
    opposite_dna += char
print(opposite_dna)
print('----------------')

1 != 2
print('----------------')

sentence = 'The e key on my keyboard is broken'
new_sentence = ''
for c in sentence:
    if c != 'e':
        new_sentence += c
print(new_sentence)
print('----------------')

1 < 2
print('----------------')

1 > 2
print('----------------')

'a' < 'b'
print('----------------')

percentage = 73
if percentage < 40:
    grade = 'F'
elif percentage < 60:
    grade = 'C'
elif percentage < 80:
    grade = 'B'
else:
    grade = 'A'
print(grade)
print('----------------')

x1 = 30
x2 = 10
x3 = 20
first = ''
if x1 < x2:
    if x1 < x3:
        first = x1
    else:
        first = x3
else:
    if x2 < x3:
        first = x2
    else:
        first = x3
print(first)
print('----------------')

first = x1
if x2 < first:
    first = x2
if x3 < first:
    first = x3
print(first)
print('----------------')

x1 = 'Charlie'
x2 = 'Alice'
x3 = 'Bob'
first = ''
if x1 < x2:
    if x1 < x3:
        first = x1
    else:
        first = x3
else:
    if x2 < x3:
        first = x2
    else:
        first = x3
print(first)
print('----------------')