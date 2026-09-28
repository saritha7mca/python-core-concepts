# Create the tuple
technologies = ("Python", "Java", "Python", "C++", "JavaScript", "Python")

# 1. Print the tuple
print("Tuple:", technologies)
# A tuple is like a list, but it cannot be changed.

# 2. Print its type
print("Type:", type(technologies))
# type() confirms it is a tuple.

# 3. Print the first item
print("First item:", technologies[0])
# [0] gives the first element.

# 4. Print the last item
print("Last item:", technologies[-1])
# [-1] gives the last element.

# 5. Slice the tuple
print("Slice (1 to 4):", technologies[1:4])
# Slicing works the same as lists: start at index 1, stop before index 4.

# 6. Count "Python"
print("Count of 'Python':", technologies.count("Python"))
# count() tells how many times a value appears.

# 7. Find the index of "C++"
print("Index of 'C++':", technologies.index("C++"))
# index() tells the position of the first match.

# 8. Find the tuple length
print("Length:", len(technologies))
# len() counts total items.

# 9. Convert the tuple into a list
tech_list = list(technologies)
print("Converted to list:", tech_list)
# list() allows us to modify the data.

# 10. Add "Go" after converting it into a list
tech_list.append("Go")
print("After adding Go:", tech_list)
# append() works only on lists, not tuples.

# 11. Convert it back into a tuple
technologies = tuple(tech_list)
print("Converted back to tuple:", technologies)
# tuple() freezes the list again into an immutable tuple.


# ----------------------------------------------------
# WHY TUPLES ARE CALLED IMMUTABLE (Short Explanation)
# ----------------------------------------------------

# Tuples are called IMMUTABLE because:
# - You cannot change their values after creation.
# - You cannot add, remove, or update items directly.
# - They stay fixed and protected once created.

# Example:
# technologies[0] = "Ruby"  → This will give an error.
# Lists can change, but tuples cannot.