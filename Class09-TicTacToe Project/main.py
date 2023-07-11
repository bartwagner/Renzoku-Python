def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def row_winner(board):
    for row in board:
        all_equal = True
        piece = row[0]
        print(row)  # check the row
        print(row[0])  # check the row
        for entry in row:
            if entry == ' ' or piece != entry:
                all_equal = False
                print(entry)  # check piece
                break
        if all_equal:
            print(all_equal)
            return True
    return False
assert_equal(
    row_winner(
        [
            ['A', 'A', 'B', 'A'],
            [' ', ' ', ' ', ' '],
            ['A', ' ', ' ', 'A'],
            ['B', ' ', 'B', 'A']
        ]
    ),
    False
)
assert_equal(
    row_winner(
        [
            ['X', ' ', 'X'],
            ['O', 'X', 'X'],
            ['O', 'O', 'O']
        ]
    ),
    True
)
print('-----------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def column_winner(board):
    for col in range(len(board[0])):
        all_equal = True
        piece = board[0][col]
        print(board)  # check the row
        for row in board:
            print(row[col]) # check column
            if row[col] == ' ' or row[col] != piece:
                all_equal = False
                break
        if all_equal:
            print(all_equal)
            return True
    return False
assert_equal(
    column_winner(
        [
            ['X', 'O', ' '],
            ['X', 'O', ' '],
            ['O', 'X', ' ']
        ]
    ),
    False
)
assert_equal(
    column_winner(
        [
            ['X', 'O', ' ', 'X'],
            [' ', 'O', 'X', 'O'],
            ['O', 'O', 'X', 'X'],
            ['O', 'O', 'X', ' ']
        ]
    ),
    True
)
print('-----------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def diagonal_winner(board):
    all_equal1 = True
    all_equal2 = True
    topleft  = board[0][0]
    topright = board[0][-1]
    for i in range(len(board)):
        if board[i][i] == ' ' or board[i][i] != topleft:
            all_equal1 = False
        if board[i][-i -1] == ' ' or board[i][-i -1] != topright:
            all_equal2 =False
    return all_equal1 or all_equal2
assert_equal(
    diagonal_winner(
        [
            ['O', 'X', 'O', 'X'],
            [' ', 'O', 'X', ' '],
            ['X', 'X', ' ', 'X'],
            ['X', ' ', 'O', 'O']
        ]
    ),
    True
)
assert_equal(
    diagonal_winner(
        [
            ['X', 'X', ' '],
            ['X', ' ', 'O'],
            [' ', 'O', 'O']
        ]
    ),
    False
)
print('-----------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def winner(board):
    row = row_winner(board)
    column  = column_winner(board)
    diagonal = diagonal_winner(board)
    return row or column or diagonal
def winning_line(strings):
    piece = strings[0]
    if piece == ' ':
        return False
    for entry in strings:
        if piece != entry:
            return False
    return True
def row_winner(board):
    for row in board:
        if winning_line(row):
            return True
    return False
def column_winner(board):
    for col in range(len(board[0])):
        column = []
        for row in board:
            column.append(row[col])
        if winning_line(column):
            return True
    return False
def diagonal_winner(board):
    diagonal1 = []
    diagonal2 = []
    for i in range(len(board)):
        diagonal1.append(board[i][i])
        diagonal2.append(board[i][-i-1])
    return winning_line(diagonal1) or winning_line(diagonal2)
assert_equal(
    winner(
        [
            ['X', 'X', 'X', ' '],
            ['X', 'X', ' ', ' '],
            ['X', ' ', 'O', 'X'],
            [' ', ' ', 'O', 'X']
        ]
    ),
    False
)
assert_equal(
    winner(
        [
            ['X', ' ', 'X'],
            ['O', 'X', 'O'],
            ['O', 'O', 'O']
        ]
    ),
    True
)
assert_equal(
    winner(
        [
            ['X', ' '],
            ['X', 'O']
        ]
    ),
    True
)
print('-----------------------')

def print_board(board):
    for row in board:
        print("".join(row))
print_board([
    ['X', 'O', 'X'],
    [' ', 'O', 'O'],
    [' ', 'X', ' ']
])
print('-----------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def format_board(board):
    string = ""
    loop = len(board)
    count = 0
    for row in board:
         string +="".join(row)
         count += 1
         if loop > count:
             string +="\n     "
    return string
assert_equal(
    format_board([
        ['X', 'O', 'X'],
        [' ', 'O', 'O'],
        [' ', 'X', ' ']
    ]),
    """XOX
      OO
      X """
)
print('-----------------------')

string = """First line
Second line"""
print(string)
print('-----------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def format_board(board):
    string  = ""
    countN  = len(board)
    countIf = 0
    for row in board:
        string += "".join(row)
        countIf += 1
        if countN > countIf:
            string +="\n"
    return string
assert_equal(
    format_board([
        ['X', 'O', 'X'],
        ['O', ' ', ' '],
        [' ', 'X', 'O']
    ]),
    'XOX\nO  \n XO'
)
print('-----------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def format_board(board):
    result = ''
    for i in range(len(board)):
        for char in board[i]:
            result += char
        if i != len(board) - 1:
            result += '\n'
    return result
assert_equal(
    format_board([
        ['X', 'O', 'X'],
        ['O', ' ', ' '],
        [' ', 'X', 'O']
    ]),
    'XOX\nO  \n XO'
)
print('-----------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def format_board(board):
    joined_rows = []
    for row in board:
        joined_rows.append("".join(row))
    return "\n".join(joined_rows)
assert_equal(
    format_board([
        ['X', 'O', 'X'],
        ['O', ' ', ' '],
        [' ', 'X', 'O']
    ]),
    'XOX\nO  \n XO'
)
print('-----------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def format_board(board):
    result = ''
    countSplit = 0
    for i in range(len(board)):
        for char in board[i]:
            result += char
            if len(board) - 1 > countSplit:
                result += "|"
                countSplit += 1
        if i != len(board) - 1:
            result += '\n-+-+-\n'
            countSplit = 0
    return result
assert_equal(
    format_board([
        ['X', 'O', 'X'],
        ['O', ' ', ' '],
        [' ', 'X', 'O']
    ]),
    'X|O|X\n-+-+-\nO| | \n-+-+-\n |X|O'
)
print('-----------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def format_board(board):
    joined_rows = []
    for row in board:
        joined_rows.append("|".join(row))
    lines = []
    for _ in board[0]:
        lines.append("-")
    line = f'\n{"+".join(lines)}\n'
    return line.join(joined_rows)
assert_equal(
    format_board([
        ['X', 'O', 'X'],
        ['O', ' ', ' '],
        [' ', 'X', 'O']
    ]),
    'X|O|X\n-+-+-\nO| | \n-+-+-\n |X|O'
)
print('-----------------------')

print(type('Hello World'))
print(type(23))
print(type(True))
print(type([1, 2, 3]))
print(type(4.56))
print('-----------------------')

print(type(3) == int)
print('-----------------------')

print(type('123'))
print(type(123))
print(123 == '123')
print('-----------------------')

print(123 + 456)
print('123' + '456')
print('-----------------------')

print(13 < 120)
print('13' < '120')
print('-----------------------')

print(sorted([120, 13, 0]))
print(sorted(['120', '13', '0']))
print('-----------------------')

number = '3'
for i in range(int(number)):
    print('Starting...', i + 1)
print('Go!')
print('-----------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def format_board(board):
    first_row = ' '
    for i in range(len(board)):
        first_row += str(i + 1)
    joined_rows = [first_row]
    for i in range(len(board)):
        joined_row = str(i + 1) + ''.join(board[i])
        joined_rows.append(joined_row)
    return "\n".join(joined_rows)
assert_equal(
    format_board([
        ['X', 'O', 'X'],
        ['O', ' ', ' '],
        [' ', 'X', 'O']
    ]),
    ' 123\n1XOX\n2O  \n3 XO'
)
print('-----------------------')

print('Type your name, then press Enter:')
name = input()
print(f'Hello {name}!')
print('-----------------------')

super_secret_number = 7
print("What number am I thinking of?")
guess = int(input())
if guess == super_secret_number:
    print("Amazing! Are you psychic?")
else:
    print("Nope!")
print('-----------------------')

def play_move(board, player):
    board[1] = player
def play_game():
    game_board = [" ", " ", " "]
    play_move(game_board, "X")
    print(game_board)
play_game()
print('-----------------------')

def play_move(board, player):
    row = board[1]
    row[0] = player
def play_game():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    play_move(board, "X")
    print(board)
play_game()
print('-----------------------')

def format_board(board):
    first_row = ' '
    for i in range(len(board)):
        first_row += str(i + 1)
    joined_rows = [first_row]
    for i in range(len(board)):
        joined_row = str(i + 1) + ''.join(board[i])
        joined_rows.append(joined_row)
    return "\n".join(joined_rows)
def play_game():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    print(format_board(board))
    print('\nX to play:\n')
    play_move(board, 'X')
    print(format_board(board))
    print('\nO to play:\n')
    play_move(board, 'O')
    print(format_board(board))
def play_move(board, player):
    row = int(input()) -1
    col = int(input()) -1
    board[row][col] = player
play_game()
print('-----------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def make_board(size):
    row = []
    for _ in range(size):
        row.append(' ')
    board = []
    for _ in range(size):
        board.append(row)
    return board
def test():
    board = make_board(3)
    assert_equal(board, [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ])
    board[0][0] = 'X'
    assert_equal(board, [
        ['X', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ])
test()
print('-----------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def make_board(size):
    board = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(' ')
        board.append(row)
    return board
def test():
    board = make_board(3)
    assert_equal(board, [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ])
    board[0][0] = 'X'
    assert_equal(board, [
        ['X', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ])
test()
print('-----------------------')

def make_board(size):
    row = []
    for _ in range(size):
        row.append(' ')
    board = []
    for _ in range(size):
        board.append(row.copy())
    return board
def make_cube(size):
    cube = []
    board = make_board(size)
    for _ in range(size):
        cube.append(board.copy())
    return cube
def test():
    cube = make_cube(2)
    print(cube)
    cube[0][0][0] = 'X'
    print(cube)
    print(cube[0] is cube[1])
    print(cube[0][0] is cube[0][1])
    print(cube[0][0] is cube[1][0])
test()
print('-----------------------')

def winning_line(strings):
    strings = set(strings)
    return len(strings) == 1 and ' ' not in strings
def row_winner(board):
    return any(winning_line(row) for row in board)
def column_winner(board):
    return row_winner(zip(*board))
def main_diagonal_winner(board):
    return winning_line(row[i] for i, row in enumerate(board))
def diagonal_winner(board):
    return main_diagonal_winner(board) or main_diagonal_winner(reversed(board))
def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)
def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'
def play_move(board, player):
    print(f'{player} to play:')
    row = int(input()) - 1
    col = int(input()) - 1
    board[row][col] = player
    print(format_board(board))
def make_board(size):
    return [[' '] * size for _ in range(size)]
def print_winner(player):
    print(f'{player} wins!')
def print_draw():
    print("It's a draw!")
def play_game(board_size, player1, player2):
    board = make_board(board_size)
    print(format_board(board))
    play_move(board, player1)
    play_move(board, player2)
    play_move(board, player1)
    play_move(board, player2)
play_game(3, 'X', 'O')
print('-----------------------')

def winning_line(strings):
    strings = set(strings)
    return len(strings) == 1 and ' ' not in strings
def row_winner(board):
    return any(winning_line(row) for row in board)
def column_winner(board):
    return row_winner(zip(*board))
def main_diagonal_winner(board):
    return winning_line(row[i] for i, row in enumerate(board))
def diagonal_winner(board):
    return main_diagonal_winner(board) or main_diagonal_winner(reversed(board))
def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)
def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'
def play_move(board, player):
    print(f'{player} to play:')
    row = int(input()) - 1
    col = int(input()) - 1
    board[row][col] = player
    print(format_board(board))
def make_board(size):
    return [[' '] * size for _ in range(size)]
def print_winner(player):
    print(f'{player} wins!')
def print_draw():
    print("It's a draw!")
def play_game(board_size, player1, player2):
    board = make_board(board_size)
    print(format_board(board))
    player = player1
    for _ in range(board_size * board_size):
        play_move(board, player)
        if winner(board):
            print_winner(player)
            return
        if player == player1:
            player = player2
        else:
            player = player1
    print_draw()
play_game(3, 'X', 'O')
print('-----------------------')