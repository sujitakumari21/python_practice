# ==========================================
#       PYTHON STRING FUNCTIONS
# ==========================================

# Creating a string
s = "  Hello Python World  "

# 1. len() - Finds the length of the string
print("1. Length:", len(s))

# 2. upper() - Converts all letters to uppercase
print("2. Uppercase:", s.upper())

# 3. lower() - Converts all letters to lowercase
print("3. Lowercase:", s.lower())

# 4. capitalize() - Converts the first character to uppercase
print("4. Capitalize:", s.capitalize())

# 5. title() - Converts the first letter of each word to uppercase
print("5. Title:", s.title())

# 6. strip() - Removes spaces from both sides
print("6. Strip:", s.strip())

# 7. lstrip() - Removes spaces from the left side
print("7. Left Strip:", s.lstrip())

# 8. rstrip() - Removes spaces from the right side
print("8. Right Strip:", s.rstrip())

# 9. replace() - Replaces one string with another
print("9. Replace:", s.replace("Python", "Java"))

# 10. find() - Returns the position of a substring
print("10. Find:", s.find("Python"))

# 11. index() - Returns the position of a substring
print("11. Index:", s.index("Python"))

# 12. count() - Counts how many times a character occurs
print("12. Count:", s.count("o"))

# 13. startswith() - Checks whether string starts with given text
print("13. Starts With:", s.startswith("  Hello"))

# 14. endswith() - Checks whether string ends with given text
print("14. Ends With:", s.endswith("  "))

# 15. split() - Splits a string into a list
print("15. Split:", s.split())

# 16. join() - Joins elements of a list into a string
words = ["I", "Love", "Python"]
print("16. Join:", " ".join(words))

# 17. isalpha() - Checks whether all characters are alphabets
print("17. Is Alpha:", "Python".isalpha())

# 18. isdigit() - Checks whether all characters are digits
print("18. Is Digit:", "12345".isdigit())

# 19. isalnum() - Checks whether characters are letters or numbers
print("19. Is Alphanumeric:", "Python123".isalnum())

# 20. isspace() - Checks whether string contains only spaces
print("20. Is Space:", "   ".isspace())

# 21. islower() - Checks whether all letters are lowercase
print("21. Is Lower:", "hello".islower())

# 22. isupper() - Checks whether all letters are uppercase
print("22. Is Upper:", "HELLO".isupper())

# 23. swapcase() - Converts uppercase to lowercase and vice versa
print("23. Swap Case:", "Hello Python".swapcase())

# 24. center() - Places the string in the center
print("24. Center:", "Python".center(20, "-"))

# 25. zfill() - Adds zeros to the left side
print("25. Zfill:", "25".zfill(5))