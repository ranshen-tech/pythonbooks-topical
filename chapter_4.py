def squared(x):
    return x ** 2

print(squared(2))

def print_string(string):
    print(string)

print_string('Testing: 1, 2, 3')


def add_mult(a, b, c, x=100, z=1000):
    return a + b + c * x * z

result = add_mult(10, 15, 25)
print(result)