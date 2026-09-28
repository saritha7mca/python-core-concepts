# Create the nested dictionary
employee = {
    "name": "Amit",
    "department": "Engineering",
    "skills": {
        "language": "Python",
        "database": "PostgreSQL",
        "cloud": "AWS"
    },
    "salary": 80000
}

# 1. Print employee name
print("Employee Name:", employee["name"])
# Access top-level key directly

# 2. Print department
print("Department:", employee["department"])
# Another top-level key

# 3. Print complete skills dictionary
print("Skills Dictionary:", employee["skills"])
# "skills" itself is another dictionary inside the main dictionary

# 4. Print programming language
print("Programming Language:", employee["skills"]["language"])
# First access "skills", then access "language" inside it

# 5. Print database
print("Database:", employee["skills"]["database"])
# Same nested access pattern

# 6. Print cloud technology
print("Cloud Technology:", employee["skills"]["cloud"])
# Accessing nested dictionary values

# 7. Change "Python" to "Python + JavaScript"
employee["skills"]["language"] = "Python + JavaScript"
print("Updated Language:", employee["skills"]["language"])
# Updating a value inside the nested dictionary

# 8. Change salary
employee["salary"] = 90000
print("Updated Salary:", employee["salary"])
# Updating a top-level key

# 9. Add "experience": 3
employee["experience"] = 3
print("Added Experience:", employee["experience"])
# Adding a new key-value pair

# 10. Add another skill under the skills dictionary
employee["skills"]["devops"] = "Docker"
print("Updated Skills:", employee["skills"])
# Adding a new key inside the nested dictionary


# ----------------------------------------------------
# EXPLANATION OF NESTED DICTIONARIES (Short & Simple)
# ----------------------------------------------------

# A nested dictionary means a dictionary inside another dictionary.
# Example:
# employee["skills"] → gives the inner dictionary
# employee["skills"]["language"] → goes inside "skills" and gets "language"

# Think of it like:
# - The main dictionary is a big folder.
# - Inside it, "skills" is a smaller folder.
# - Inside that folder, "language", "database", "cloud" are files.

# To access nested values:
# Step 1: Open the outer dictionary using its key.
# Step 2: Open the inner dictionary using its key.
# Example:
# employee["skills"]["cloud"]
# First opens "skills", then gets "cloud".