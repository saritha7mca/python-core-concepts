def add_print(a, b):
    """Prints the result instead of returning it."""
    print(a + b)

add_print(10, 20)


def add_return(a, b):
    """Returns the result so it can be reused."""
    return a + b

result = add_return(10, 20)
print("Result:", result)
print("Result doubled:", result * 2)

# Why return is useful
# Because return gives you a value you can reuse, while print() only displays it.