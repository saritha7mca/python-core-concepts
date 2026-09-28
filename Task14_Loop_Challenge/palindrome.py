text = "madam"
reverse = ""

for ch in text:
    reverse = ch + reverse   # building reversed string

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
