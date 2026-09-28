# Create the string
student = "python programming for data science"


# 1. Print the complete string
print("Complete string:", student)

# 2. Print the first character
print("First character:", student[0])

# 3. Print the last character
print("Last character:",student[-1])

# 4. Print the first 6 characters
print("First 6 characters:", student[:6])

# 5. Print the last 7 characters
print("Last 7 characters:", student[-7:])

# 6. Reverse the string using slicing
print("Reversed:", student[::-1])
# [::-1] flips the string backwards

# 7. Convert it to uppercase
print("Uppercase:", student.upper())  
# upper() makes all letters BIG

# 8. Convert it to lowercase
print("Lowercase:", student.lower())  
# lower() makes all letters small

# 9. Convert it to title case
print("Title case:", student.title())  
# title() makes the first letter of each word uppercase

# 10. Count how many times 'a' appears
print("Count of 'a':", student.count("a"))  
# count() tells how many times a letter appears


# 11. Find the position of 'programming'
print("Position of 'programming':", student.find("programming"))  
# find() tells where a word starts

# 12. Replace 'data science' with 'artificial intelligence'
print("Replaced:", student.replace("data science", "artificial intelligence"))  
# replace() swaps one phrase with another

# 13. Split the string into individual words
print("Split into words:", student.split())  
# split() breaks the sentence into separate words