def is_prime(n):
    """Return True if n is prime, else False."""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(17))
