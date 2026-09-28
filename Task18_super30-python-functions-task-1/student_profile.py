def student_profile(name, age, course):
    """Return a formatted student profile."""
    return f"Name: {name}, Age: {age}, Course: {course}"

# Positional arguments
print(student_profile("Rahul", 22, "Python"))

# Keyword arguments
print(student_profile(name="Priya", age=21, course="Data Science"))
