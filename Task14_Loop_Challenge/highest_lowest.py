transactions = [1200, 450, 800, 1500, 2300, 700, 100]

highest = transactions[0]
lowest = transactions[0]

for t in transactions:
    if t > highest:
        highest = t
    if t < lowest:
        lowest = t

print("Highest:", highest)
print("Lowest:", lowest)
