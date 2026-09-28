# Create the sets
python_students = {"Rahul", "Aman", "Priya", "Karan", "Neha"}
java_students = {"Priya", "Karan", "Rohit", "Simran"}

# 1. Print both sets
print("Python students:", python_students)
print("Java students:", java_students)
# Sets show unique values only and do not keep order


# 2. Students learning either Python or Java
print("Either Python or Java:", python_students.union(java_students))
# union() combines both sets and removes duplicates


# 3. Students learning both
print("Both Python and Java:", python_students.intersection(java_students))
# intersection() gives only the common names


# 4. Students learning only Python
print("Only Python:", python_students.difference(java_students))
# difference() shows names in Python set that are NOT in Java set


# 5. Students learning only Java
print("Only Java:", java_students.difference(python_students))
# Same idea but reversed


# 6. Students belonging to exactly one group
print("Exactly one group:", python_students.symmetric_difference(java_students))
# symmetric_difference() gives names that are NOT shared


# 7. Add a new student
python_students.add("Sneha")
print("After adding Sneha:", python_students)
# add() inserts a new item into the set


# 8. Remove a student
python_students.remove("Rahul")
print("After removing Rahul:", python_students)
# remove() deletes an item but gives an error if the item is missing


# 9. Demonstrate discard()
python_students.discard("Aman")
print("After discarding Aman:", python_students)
# discard() also deletes an item but does NOT give an error if missing


# ----------------------------------------------------
# EXPLANATION OF SET METHODS (Short & Simple)
# ----------------------------------------------------

# union()               → Combines two sets, removes duplicates
# intersection()        → Gives common items in both sets
# difference()          → Items in one set but not the other
# symmetric_difference()→ Items that are NOT shared between sets

# add()                 → Adds a new item to the set
# remove()              → Removes an item; ERROR if item not found
# discard()             → Removes an item; NO ERROR if item not found

# ----------------------------------------------------
# WHY SETS ARE USEFUL
# ----------------------------------------------------
# Sets are great when:
# - You want only unique values
# - You want to remove duplicates automatically
# - You need fast membership checking (is "Priya" in the set?)
# - You want to compare groups (common, different, unique items)