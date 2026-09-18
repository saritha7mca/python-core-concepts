message = "Welcome To Python Programming Class "

# Remove Extra Spaces
message = message.strip()
print(message)

# Convert everything to lowercase
message = message.lower()
print(message)

# Convert everything to uppercase
message = message.upper()
print(message)

# COnvert to Title Case
message = message.title()
print(message)

#Replace "Python" with "Advanced Python"
message = message.replace("Python", "Advanced Python")
print(message)

#Check whether the string starts with "Welcome"
if message.startswith("Welcome"):
    print("Yes, the string starts with 'Welcome'")
else:
    print("NO, the string does not starts with 'welcome'")

#Check whether it ends with "Class"
if message.endswith("Class"):
    print("Yes, the string ends with 'Class'")
else:
    print("No, the string ends with 'Class'")

#Count occurrences of "o"
count_O = message.count("o")
print("count_O")

#Find the position of "Programming"
position = message.find("Programming")
print(position)

#words = message.split()
words = message.split()
print(words)
