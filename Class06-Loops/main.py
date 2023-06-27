for letter in "ABC":
    print(letter)
    for number in range(4):
        print(f'{letter} {number}')
    print('---')
print('----------------')

for numbers in range(1,13):
    for number in range(1,13):
        print(f'{numbers} x {number} = {number * numbers}')
    print('---')
print('----------------')

players = ["Alice", "Bob", "Charlie"]
for player in players:
    for player2 in players:
        if player is not player2:
            print(f'{player} vs {player2}')
print('----------------')

letters = "ABCD"
for letter in letters:
    for letter2 in letters:
        for letter3 in letters:
            for letter4 in letters:
                print(f'{letter}{letter2}{letter3}{letter4}')
print('----------------')

size = 5
for i in range(size):
    length = size - i
    line = ''
    for _ in range(length):
        line += '+'
    print(line)
print('----------------')

players = ['Charlie', 'Alice', 'Dylan', 'Bob']
for player in players.copy():
    for player2 in players:
        if player is not player2:
            print(f"{player} vs {player2}")
    players.remove(player)
print('----------------')

players = ['Charlie', 'Alice', 'Dylan', 'Bob']
for i in range(len(players)):
    for j in range(len(players)):
        if i < j:
            print(f'{players[i]} vs {players[j]}')
print('----------------')

a = 2
b = 3
c = 4
d = 5
print(a * b + c * d)
print('----------------')

word = 'Amazing'
vowels = []
consonants = []
for letter in word:
    if letter.lower() in 'aeiou':
        vowels.append(letter)
    else:
        consonants.append(letter)
print(vowels)
print(consonants)
print('----------------')

strings = ["abc", "def", "ghi"]
string = strings[1]
print(string[0])
print('----------------')

strings = ["abc", "def", "ghi"]
print(strings[1][0])
print('----------------')

strings = strings = ["abc", "def", "ghi"]
print(strings[-2][-1])
print('----------------')

strings = [['hello', 'there'], ['how', 'are', 'you']]
print(strings[1][0])
print('----------------')

strings = [['hello', 'there'], ['how', 'are', 'you']]
print(strings[1][2][0])
print('----------------')

strings = [['hello', 'there'], ['how', 'are', 'you']]
strings[1].append("today?")
print(strings)
print('----------------')

numbers = [[1, 2, 3], [4, 5], [6], []]
for sublist in numbers:
    for num in sublist:
        print(num)
    print('---')
print('----------------')


print('----------------')
print('----------------')