n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i   # multiplying step-by-step

print("Factorial =", fact)
