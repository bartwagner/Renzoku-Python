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

