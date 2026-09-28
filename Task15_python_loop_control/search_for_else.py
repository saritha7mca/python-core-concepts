numbers = [10, 20, 30, 40, 50]
target = int(input("Enter number to search: "))

for n in numbers:
    if n == target:
        print("Number Found")
        break
else:
    print("Number Not Found")
