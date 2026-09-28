# Create the student dictionary
student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python",
    "city": "Bangalore",
    "marks": 88
}

# 1. Print the complete dictionary
print("Complete dictionary:", student)
# Shows all key-value pairs

# 2. Print the student's name
print("Name:", student["name"])
# Accessing value using its key

# 3. Print their course
print("Course:", student["course"])

# 4. Print all keys
print("Keys:", student.keys())
# keys() returns all the keys in the dictionary

# 5. Print all values
print("Values:", student.values())
# values() returns all the values

# 6. Print all key-value pairs
print("Items:", student.items())
# items() returns key-value pairs as tuples

# 7. Change marks from 88 to 92
student["marks"] = 92
print("Updated marks:", student["marks"])
# Updating a value inside the dictionary

# 8. Add "email"
student["email"] = "rahul@example.com"
print("Added email:", student["email"])

# 9. Add "phone"
student["phone"] = "9876543210"
print("Added phone:", student["phone"])

# 10. Remove "city"
student.pop("city")
print("After removing city:", student)
# pop() removes a key-value pair

# 11. Use get() to retrieve "name"
print("Name using get():", student.get("name"))
# get() safely retrieves a value; returns None if key doesn't exist

# 12. Create a copy of the dictionary
student_copy = student.copy()
print("Copied dictionary:", student_copy)
# copy() creates a separate duplicate dictionary


# ----------------------------------------------------
# EXPLANATION OF DICTIONARY METHODS (Short & Simple)
# ----------------------------------------------------

# keys()   → Shows all the keys in the dictionary
# values() → Shows all the values
# items()  → Shows key-value pairs together
# get()    → Safely gets a value; does NOT give an error if key is missing
# update() → Changes or adds multiple key-value pairs at once
# pop()    → Removes a key-value pair
# copy()   → Makes a separate duplicate dictionary

# Example of update():
# student.update({"marks": 95, "city": "Mumbai"})
# This updates multiple values at the same time.