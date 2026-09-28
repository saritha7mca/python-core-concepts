secret = 42
guess = None

while guess != secret:
    guess = int(input("Guess the number: "))
    if guess != secret:
        print("Wrong, try again")

print("Correct guess!")
