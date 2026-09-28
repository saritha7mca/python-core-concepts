numbers = [12, 7, 9, 20, 33, 42, 8, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)
