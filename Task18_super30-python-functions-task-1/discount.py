def calculate_discount(price, discount=10):
    """Return price after applying discount percentage."""
    return price - (price * discount / 100)

print(calculate_discount(1000))        # uses default 10%
print(calculate_discount(1000, 20))    # custom discount
