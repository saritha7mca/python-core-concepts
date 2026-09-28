balance = 5000

def check_balance():
    print("Current balance:", balance)

def deposit():
    global balance
    amt = int(input("Enter amount to deposit: "))
    balance += amt
    print("Deposited:", amt)

def withdraw():
    global balance
    amt = int(input("Enter amount to withdraw: "))
    if amt <= balance:
        balance -= amt
        print("Withdrawn:", amt)
    else:
        print("Insufficient balance.")

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice.")
