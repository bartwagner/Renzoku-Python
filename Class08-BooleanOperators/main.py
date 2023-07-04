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