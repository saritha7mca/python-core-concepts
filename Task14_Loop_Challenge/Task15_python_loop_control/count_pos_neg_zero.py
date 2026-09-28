numbers = [10, -4, 8, -2, 0, 15, -9, 21]

pos = neg = zero = 0

for n in numbers:
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    else:
        zero += 1

print("Positive:", pos)
print("Negative:", neg)
print("Zeros:", zero)
