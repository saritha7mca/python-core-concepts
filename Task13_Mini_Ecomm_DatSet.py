# Create a list of dictionaries (3 products)
products = [
    {
        "name": "Laptop",
        "price": 70000,
        "brand": "Dell"
    },
    {
        "name": "Phone",
        "price": 40000,
        "brand": "Samsung"
    },
    {
        "name": "Tablet",
        "price": 30000,
        "brand": "Apple"
    }
]

# 1. Print all products
print("All products:", products)
# A list containing 3 dictionaries

# 2. Print first product
print("First product:", products[0])
# products[0] selects the first dictionary

# 3. Print second product's price
print("Second product price:", products[1]["price"])
# products[1] selects second dictionary, ["price"] selects its price

# 4. Print third product's brand
print("Third product brand:", products[2]["brand"])
# products[2] selects third dictionary, ["brand"] selects its brand

# 5. Change first product's price
products[0]["price"] = 75000
print("Updated first product price:", products[0]["price"])
# Updating a value inside a dictionary

# 6. Add "rating" to the second product
products[1]["rating"] = 4.5
print("Second product with rating:", products[1])
# Adding a new key-value pair

# 7. Add another product manually
products.append({
    "name": "Smartwatch",
    "price": 15000,
    "brand": "Fitbit"
})
print("After adding new product:", products)
# append() adds a new dictionary to the list

# 8. Print the final dataset
print("Final dataset:", products)
# Shows all products including the new one


# ----------------------------------------------------
# EXPLANATION (Short & Simple)
# ----------------------------------------------------

# LIST:
# A list stores multiple items in order.
# Here, each item is a dictionary.
# Example: products[0] → first dictionary

# DICTIONARY:
# A dictionary stores data in key-value pairs.
# Example: {"name": "Laptop", "price": 70000}

# INDEXING:
# Used to pick items from the list.
# products[1] → second product

# KEYS:
# Keys are the labels inside a dictionary.
# Example: "name", "price", "brand"

# VALUES:
# Values are the data stored inside each key.
# Example: "Laptop", 70000, "Dell"

# Together:
# products[1]["price"]
# First pick the second dictionary, then pick its price.
