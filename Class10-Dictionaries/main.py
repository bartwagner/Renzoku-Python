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

