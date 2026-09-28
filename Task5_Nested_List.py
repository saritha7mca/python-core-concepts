# Create the nested list of students
students = [
    ["Rahul", 21, "Python"],            # students[0]
    ["Priya", 22, "Data Science"],      # students[1]
    ["Aman", 20, "Machine Learning"]    # students[2]
]

# 1. Print the complete list
print("Complete list:", students)
# This prints the entire nested list with all student records.

# 2. Print Rahul's name
print("Rahul's name:", students[0][0])
# students[0] selects Rahul's record.
# [0] inside that record selects his name.

# 3. Print Priya's age
print("Priya's age:", students[1][1])
# students[1] selects Priya's record.
# [1] inside that record selects her age.

# 4. Print Aman's course
print("Aman's course:", students[2][2])
# students[2] selects Aman's record.
# [2] inside that record selects his course.

# 5. Print the complete record of Priya
print("Priya's record:", students[1])
# students[1] gives the entire list: ["Priya", 22, "Data Science"]

# 6. Change Rahul's course to "AI"
students[0][2] = "AI"
# students[0] selects Rahul.
# [2] selects his course and updates it to "AI".

# 7. Add another student record manually
students.append(["Sneha", 23, "Cyber Security"])
# append() adds a new list (new student) to the end of the nested list.

# 8. Print the updated nested list
print("Updated list:", students)
# Shows all students including the newly added one.


# -------------------------------
# EXPLANATION OF NESTED INDEXING
# -------------------------------

# A nested list is a list inside another list.
# Example:
# students = [
#     ["Rahul", 21, "Python"],
#     ["Priya", 22, "Data Science"],
#     ["Aman", 20, "Machine Learning"]
# ]

# The FIRST index chooses the student:
# students[0] → Rahul
# students[1] → Priya
# students[2] → Aman

# The SECOND index chooses the item inside that student's record:
# [0] → Name
# [1] → Age
# [2] → Course

# Example:
# students[1][2]
# students[1] = ["Priya", 22, "Data Science"]
# [2] = "Data Science"