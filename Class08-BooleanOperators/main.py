def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def is_friend(name):
    if name == "Alice":
        return True
    elif name == "Bob":
        return True
    else:
        return False
assert_equal(is_friend("Alice"), True)
assert_equal(is_friend("Bob"), True)
assert_equal(is_friend("Charlie"), False)
print('---------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def is_friend(name):
    if name == "Alice" or name == "Bob":
        return True
    else:
        return False
assert_equal(is_friend("Alice"), True)
assert_equal(is_friend("Bob"), True)
assert_equal(is_friend("Charlie"), False)
print('---------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def is_friend(name):
    return name == "Alice" or name == "Bob"
assert_equal(is_friend("Alice"), True)
assert_equal(is_friend("Bob"), True)
assert_equal(is_friend("Charlie"), False)
print('---------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def is_friend(name):
    return name == "Alice" or "Bob"
assert_equal(is_friend("Alice"), True)
assert_equal(is_friend("Bob"), True)
assert_equal(is_friend("Charlie"), False)
print('---------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def is_friend(name):
    return name in ["Alice", "Bob", "Charlie"]
assert_equal(is_friend("Alice"), True)
assert_equal(is_friend("Bob"), True)
assert_equal(is_friend("Charlie"), False)
print('---------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def is_valid_percentage(x):
    if x < 0 or x > 100:
        return False
    else:
        return True
assert_equal(is_valid_percentage(-1), False)
assert_equal(is_valid_percentage(0), True)
assert_equal(is_valid_percentage(50), True)
assert_equal(is_valid_percentage(100), True)
assert_equal(is_valid_percentage(101), False)
print('---------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def is_valid_percentage(x):
    if x >= 0 and x <= 100:
        return True
    else:
        return False
assert_equal(is_valid_percentage(-1), False)
assert_equal(is_valid_percentage(0), True)
assert_equal(is_valid_percentage(50), True)
assert_equal(is_valid_percentage(100), True)
assert_equal(is_valid_percentage(101), False)
print('---------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def all_equal(row):
    return row[0] == row[1] == row[2]
    # return row[0] == row[1] and row[0] == row[2]
    # return row == [row[0], row[0], row[0]]
assert_equal(all_equal(["X", "X", "X"]), True)
assert_equal(all_equal(["O", "O", "O"]), True)
assert_equal(all_equal(["X", "O", "X"]), False)
print('---------------------------')

name = "Bob"
is_friend = name == "Alice" or \
            name == "Bob"
print(is_friend)
is_friend = (name == "Alice" or
             name == "Bob")
print(is_friend)
is_friend = [name == "Alice",
             name == "Bob"]
print(is_friend)
print(name == "Alice" or
      name == "Bob")
print('---------------------------')

True or False and False
(True or False) and False
True or (False and False)
print('---------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def diagonal_winner(board):
    middle = board[1][1]
    return(
            (middle == board[0][0] and middle == board[2][2]) or
            (middle == board[0][2] and middle == board[2][0])
        )
assert_equal(
    diagonal_winner(
        [
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'O', 'X']
        ]
    ),
    True
)
assert_equal(
    diagonal_winner(
        [
            ['X', 'X', 'O'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']
        ]
    ),
    True
)
assert_equal(
    diagonal_winner(
        [
            ['O', 'X', 'O'],
            ['X', 'X', 'X'],
            ['O', 'O', 'X']
        ]
    ),
    False
)
print('---------------------------')

b = True
print(not b or b)
print('---------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def invalid_image(filename):
    return not (filename.endswith(".png") or filename.endswith(".jpg"))
assert_equal(invalid_image("dog.png"), False)
assert_equal(invalid_image("cat.jpg"), False)
assert_equal(invalid_image("invoice.pdf"), True)
print('---------------------------')

