correct_password = "super30"
attempts = 0

while attempts < 3:
    pwd = input("Enter password: ")

    if pwd == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect password.")
        attempts += 1

if attempts == 3:
    print("Account locked. Too many attempts.")
