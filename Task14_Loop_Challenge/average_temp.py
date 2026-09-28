temperatures = [32, 35, 28, 40, 38, 31, 42]

total = 0
for temp in temperatures:
    total += temp

average = total / len(temperatures)
print("Average temperature:", average)
