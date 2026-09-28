def largest_value(*args):
    # *args allows unlimited inputs
    largest = args[0]
    for num in args:
        if num > largest:
            largest = num
    return largest

print(largest_value(10, 50, 3, 99, 42))
