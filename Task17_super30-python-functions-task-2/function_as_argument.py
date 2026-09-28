def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(func, x, y):
    # func is another function passed as argument
    return func(x, y)

print(calculate(add, 10, 20))
print(calculate(multiply, 10, 20))
