def count_vowels(text):
    """Return number of vowels in a string."""
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("Education"))
