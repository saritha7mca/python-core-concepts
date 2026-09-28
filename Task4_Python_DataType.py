# ---------- INT ----------
age = 12
year = 2026

print(age, type(age))
print(year, type(year))

# ---------- FLOAT ----------
price = 19.99
temperature = 98.6

print(price, type(price))
print(temperature, type(temperature))

# ---------- STRING ----------
name = "Sarita"
course = "Python Programming"

print(name, type(name))
print(course, type(course))

# ---------- BOOLEAN ----------
is_student = True
is_logged_in = False

print(is_student, type(is_student))
print(is_logged_in, type(is_logged_in))

# ---------- LIST ----------
fruits = ["apple", "banana", "orange"]
scores = [95, 88, 76]

print(fruits, type(fruits))
print(scores, type(scores))

# ---------- TUPLE ----------
coordinates = (10, 20)
colors = ("red", "blue", "green")

print(coordinates, type(coordinates))
print(colors, type(colors))

# ---------- SET ----------
unique_numbers = {1, 2, 3, 4}
subjects = {"math", "science", "english"}

print(unique_numbers, type(unique_numbers))
print(subjects, type(subjects))

# ---------- DICTIONARY ----------
student_info = {"name": "John", "grade": 6}
marks = {"math": 95, "science": 88}

print(student_info, type(student_info))
print(marks, type(marks))



# 1. Convert string "100" to an integer
print(int("100"))
# Explanation: "100" is text. int() turns it into the number 100.

# 2. Convert string "45.67" to a float
print(float("45.67"))
# Explanation: "45.67" is text. float() turns it into a decimal number 45.67.

# 3. Convert number 500 to a string
print(str(500))
# Explanation: 500 is a number. str() turns it into text "500".

# 4. Convert number 1 to a boolean
print(bool(1))
# Explanation: bool(1) becomes True because any non‑zero number is True.

# 5. Convert tuple (1, 2, 3) to a list
print(list((1, 2, 3)))
# Explanation: list() turns the tuple into a list: [1, 2, 3].

# 6. Convert list [1, 2, 3] to a tuple
print(tuple([1, 2, 3]))
# Explanation: tuple() turns the list into a tuple: (1, 2, 3).

# 7. Convert list with duplicates into a set
print(set([1, 2, 2, 3]))
# Explanation: set() removes duplicates, leaving {1, 2, 3}.