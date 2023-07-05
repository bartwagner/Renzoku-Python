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

