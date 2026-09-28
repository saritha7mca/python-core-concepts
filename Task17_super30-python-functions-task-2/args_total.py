def total_values(*args):
    # *args collects any number of values into a tuple
    total = 0
    for num in args:
        total += num
    return total

print(total_values(10, 20, 30, 40))
