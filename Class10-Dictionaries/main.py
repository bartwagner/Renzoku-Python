french = {'apple': 'pomme', 'box': 'boite'}
print(french['apple'])
print(french['box'])
print('------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def total_cost(cart, prices):
    result = 0
    for item in cart:
        price = prices[item]
        result += price
    return result
assert_equal(
    total_cost(
        ['apple', 'box', 'cat'],
        {'apple': 2, 'box': 5, 'cat': 100, 'dog': 100},
    ),
    107,
)
print('------------------------')
def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def total_cost(cart, quantities, prices):
    result = 0
    for item in cart:
        price = prices[item]
        quantity = quantities[item]
        result += price * quantity
    return result
assert_equal(
    total_cost(
        ['dog', 'box'],
        {'dog': 5000000, 'box': 2},
        {'apple': 2, 'box': 5, 'cat': 100, 'dog': 100},
    ),
    500000010,
)
print('------------------------')

def substitute(string):
    result = ''
    for char in string:
        if char == 'A':
            char = 'T'
        elif char == 'T':
            char = 'A'
        elif char == 'G':
            char = 'C'
        elif char == 'C':
            char = 'G'
        result += char
    return result
original = 'AGTAGCGTCCTTAGTTACAGGATGGCTTAT'
expected = 'TCATCGCAGGAATCAATGTCCTACCGAATA'
assert_equal(substitute(original), expected)
print('------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def substitute(string, d):
    changeLetter = ''
    for item in string:
        changeLetter += d[item]
    return changeLetter
original = 'AGTAGCGTCCTTAGTTACAGGATGGCTTAT'
expected = 'TCATCGCAGGAATCAATGTCCTACCGAATA'
assert_equal(substitute(original, {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}), expected)
print('------------------------')

quantities = {'apple': 1, 'cat': 10}
print(quantities.keys())
print('------------------------')

quantities = {'apple': 1, 'cat': 10}
for key in quantities.keys():
    print(key)
print('------------------------')

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def total_cost(quantities, prices):
    result = 0
    for item in quantities.keys():
        price = prices[item]
        quantity = quantities[item]
        result += price * quantity
    return result
assert_equal(
    total_cost(
        {'dog': 5000000, 'box': 2},
        {'apple': 2, 'box': 5, 'cat': 100, 'dog': 100},
    ),
    500000010,
)
print('------------------------')

def print_words(french):
    for item in french:
        print('English: ' + item)
        print('French: ' + french[item])
        print('---')
print_words({'apple': 'pomme', 'box': 'boite'})
print('------------------------')

def print_words(french, german):
    for item in french:
        print('English: ' + item)
        print('French: ' + french[item])
        print('German: ' + german[item])
        print('---')

print_words({'apple': 'pomme', 'box': 'boite'},
            {'apple': 'apfel', 'box': 'kasten'},
)
print('------------------------')

def print_words(words):
    for word in words:
        translations = words[word]
        print(f"English: {word}")
        for language in translations:
            print(f"{language}: {translations[language]}")
        print(f"---")
print_words({
    'apple': {
        'French': 'pomme',
        'German': 'apfel',
    },
    'box': {
        'French': 'boite',
        'German': 'kasten',
    },
})
print('------------------------')