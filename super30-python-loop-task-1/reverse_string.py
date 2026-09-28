text = input("Enter a string: ")
rev = ""

for ch in text:
    rev = ch + rev   # building reversed string

print("Reversed:", rev)
