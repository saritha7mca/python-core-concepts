def factorial(n):
    # Base case
    if n == 1:
        return 1
    # Recursive call
    return n * factorial(n - 1)

print(factorial(5))
