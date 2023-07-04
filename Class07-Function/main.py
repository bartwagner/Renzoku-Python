def greet(name):
    print(f"Hello {name}!")
    print("How are you?")
greet("Alice")
greet("Bob")
print('------------------------')

def print_twice(x):
    print(f"{x}")
    print(f"{x}")
print_twice("Hello")
print('------------------------')

def print_many(thing, n):
    for _ in range(n):
        print(thing)
print_many("Hello",3)
print('------------------------')

def print_many(n, thing):
    for _ in range(n):
        print(thing)
def print_twice(x):
    print_many(2, x)
print_twice("Hello")
print('------------------------')

def double(x):
    return x * 2
number = 5
twice = double(number)
print(number)
print(twice)
print('------------------------')

def double(x):
    return x * 2
number = 5
double(number)
print(number)
print('------------------------')

def double(x):
    return x * 2
def quadruple(x):
    return double(double(x))
x = 5
print(quadruple(x))
print('------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def double(x):
    return x * 2
assert_equal(double(2), 4)
assert_equal(double(5), 10)
print('------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def double(x):
    return x * 3
assert_equal(double(2), 4)
assert_equal(double(5), 10)
print('------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def double(x):
    return x * 2
def quadruple(x):
    return double(double(x))
assert_equal(quadruple(2), 8)
assert_equal(quadruple(5), 20)
print('------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def surround(string, sides):
    return sides + string + sides
assert_equal(surround("more", "++"), "++more++")
assert_equal(surround("the same", "="), "=the same=")
print('------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def alert(string, level):
    returnNumber = ''
    for _ in range(level):
        returnNumber += '!'
    return returnNumber + " " + string + " " + returnNumber
assert_equal(alert("Warning", 2), "!! Warning !!")
assert_equal(alert("DANGER", 4), "!!!! DANGER !!!!")
print('------------------------')


def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def surround(string, sides):
    return sides + string + sides
def alert(string, level):
    string = surround(string, ' ')
    for _ in range(level):
        string = surround(string, '!')
    return string
assert_equal(alert("Warning", 2), "!! Warning !!")
assert_equal(alert("DANGER", 4), "!!!! DANGER !!!!")
print('------------------------')

def foo():
    return 1
    return 2
print(foo())
print('------------------------')
def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def double_numbers(numbers):
    for x in numbers:
        return x * 2
assert_equal(double_numbers([1, 2, 3]), [2, 4, 6])
print('------------------------')

def foo():
    for letter in 'abc':
        for number in range(3):
            print(f"{letter} {number}")
            if letter == 'b':
                return letter
foo()
print('------------------------')

def foo():
    for letter in 'abc':
        for number in range(3):
            print(f"{letter} {number}")
            if letter == 'b':
                break
foo()
print('------------------------')