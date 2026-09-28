# Create the laptop dictionary
laptop = {
    "brand": "Dell",
    "model": "XPS 15",
    "price": 120000,
    "ram": "16GB",
    "storage": "512GB SSD",
    "available": True
}

# 1. Display the product
print("Laptop details:", laptop)
# Prints the entire dictionary

# 2. Print brand
print("Brand:", laptop["brand"])
# Accessing value using its key

# 3. Print model
print("Model:", laptop["model"])

# 4. Print price
print("Price:", laptop["price"])

# 5. Change price
laptop["price"] = 110000
print("Updated Price:", laptop["price"])
# Updating a value inside the dictionary

# 6. Add processor information
laptop["processor"] = "Intel i7"
print("Added Processor:", laptop["processor"])
# Adding a new key-value pair

# 7. Add GPU information
laptop["gpu"] = "NVIDIA RTX 3050"
print("Added GPU:", laptop["gpu"])

# 8. Change RAM to "32GB"
laptop["ram"] = "32GB"
print("Updated RAM:", laptop["ram"])

# 9. Remove "available"
laptop.pop("available")
print("After removing 'available':", laptop)
# pop() removes a key-value pair

# 10. Print all keys
print("Keys:", laptop.keys())
# keys() shows all dictionary keys

# 11. Print all values
print("Values:", laptop.values())
# values() shows all dictionary values

# 12. Print all items
print("Items:", laptop.items())
# items() shows key-value pairs


# ----------------------------------------------------
# Create a second product dictionary (Mobile Phone)
# ----------------------------------------------------

mobile = {
    "brand": "Samsung",
    "model": "Galaxy S25",
    "price": 85000,
    "ram": "12GB",
    "storage": "256GB",
    "battery": "5000mAh",
    "camera": "108MP"
}

print("Mobile details:", mobile)
# Another dictionary representing a different product