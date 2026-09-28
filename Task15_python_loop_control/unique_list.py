data = [10, 20, 10, 30, 20, 40, 30]
unique = []

for item in data:
    if item not in unique:
        unique.append(item)

print(unique)
