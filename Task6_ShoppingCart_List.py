# Create the cart list
cart = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

# 1. Display all products
print("All products:", cart)
# Just prints the entire list

# 2. Access first and last products
print("First product:", cart[0])      # [0] means the first item
print("Last product:", cart[-1])      # [-1] means the last item

# 3. Add "Webcam"
cart.append("Webcam")
# append() adds an item to the END of the list

# 4. Insert "USB Hub" at index 2
cart.insert(2, "USB Hub")
# insert(index, item) places the item at a specific position

# 5. Remove "Mouse"
cart.remove("Mouse")
# remove() deletes the FIRST matching item

# 6. Remove the last item using pop()
cart.pop()
# pop() removes the last item (unless you give an index)

# 7. Find the index of "Monitor"
print("Index of Monitor:", cart.index("Monitor"))
# index() tells the position of an item

# 8. Count occurrences of "Laptop"
print("Count of Laptop:", cart.count("Laptop"))
# count() tells how many times an item appears

# 9. Create a copy of the cart
cart_copy = cart.copy()
print("Copied cart:", cart_copy)
# copy() makes a separate duplicate list

# 10. Reverse the cart
cart.reverse()
print("Reversed cart:", cart)
# reverse() flips the list order

# 11. Sort the products alphabetically
cart.sort()
print("Sorted cart:", cart)
# sort() arranges items in alphabetical order


# ----------------------------------------------------
# EXPLANATION OF LIST METHODS (Short & Simple)
# ----------------------------------------------------

# append()  → Adds one item to the END of the list
# extend()  → Adds MULTIPLE items to the end (like merging lists)
# insert()  → Adds an item at a specific index
# remove()  → Deletes the FIRST matching item
# pop()     → Removes an item by index (default: last item)
# clear()   → Removes ALL items from the list
# copy()    → Makes a new list with the same items
# sort()    → Sorts the list alphabetically or numerically
# reverse() → Reverses the order of the list