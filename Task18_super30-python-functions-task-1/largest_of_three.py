def largest_of_three(a, b, c):
    """Return the largest of three numbers."""
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

print(largest_of_three(10, 25, 7))
