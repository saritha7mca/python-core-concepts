def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

choice = 0

while choice != 5:   # condition
    print("\n--- Calculator ---")
    print("1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    print("5 Exit")

    choice = int(input("Choose: "))

    if choice == 5:
        print("Goodbye")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", sub(a, b))
    elif choice == 3:
        print("Result:", mul(a, b))
    elif choice == 4:
        print("Result:", div(a, b))
    else:
        print("Invalid choice")
