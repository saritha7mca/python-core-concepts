balance = 5000
choice = 0

while choice != 4:   # condition
    print("\n--- ATM ---")
    print("1 Check Balance")
    print("2 Deposit")
    print("3 Withdraw")
    print("4 Exit")

    choice = int(input("Choose: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amt = int(input("Enter amount: "))
        balance += amt
        print("Deposited:", amt)

    elif choice == 3:
        amt = int(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you for using ATM")

    else:
        print("Invalid choice")
