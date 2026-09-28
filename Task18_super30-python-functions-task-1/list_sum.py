def list_sum(values):
    """Return sum of all numbers in a list."""
    total = 0
    for v in values:
        total += v
    return total

print(list_sum([10, 20, 30]))
