# Create the original list
numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60]

# 1. Print the original list
print("Original list:", numbers)
# Shows all numbers including duplicates

# 2. Convert the list into a set
unique_numbers = set(numbers)
print("Set version:", unique_numbers)
# set() removes duplicates automatically

# 3. Observe which duplicates disappear
# In the set, repeated values like 10, 20, 30 appear only once

# 4. Convert the set back into a list
new_list = list(unique_numbers)
print("Converted back to list:", new_list)
# list() turns the set into a list again

# 5. Print the number of original elements
print("Original count:", len(numbers))
# len() counts total items including duplicates

# 6. Print the number of unique elements
print("Unique count:", len(unique_numbers))
# len() on a set counts only unique items

# 7. Another example using duplicate student names
students = ["Rahul", "Priya", "Rahul", "Aman", "Priya", "Sneha"]
print("Original students:", students)

unique_students = set(students)
print("Unique students:", unique_students)
# Duplicate names like Rahul and Priya appear only once in the set


# ----------------------------------------------------
# WHY SETS ARE USEFUL (Short Explanation)
# ----------------------------------------------------

# Sets are useful because:
# - They automatically remove duplicates.
# - They help when you want only unique values.
# - They are great for checking membership quickly.
# - They keep data clean when duplicates cause problems.

# Example:
# If a class attendance list has repeated names,
# converting it to a set gives you the unique students.