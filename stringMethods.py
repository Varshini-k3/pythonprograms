# A complete program demonstrating common Python string methods

# 1. Original text with messy whitespace
raw_text = "   Welcome to Python Programming!   "
print(f"Original text: '{raw_text}'")

# 2. Removing leading and trailing whitespace using strip()
cleaned_text = raw_text.strip()
print(f"After strip(): '{cleaned_text}'")

# 3. Changing text case using upper(), lower()
print(f"Uppercase:     {cleaned_text.upper()}")
print(f"Lowercase:     {cleaned_text.lower()}")

# 4. Checking prefixes and suffixes using startswith() and endswith()
print(f"Starts with 'Welcome'? {cleaned_text.startswith('Welcome')}")
print(f"Ends with 'Java'?      {cleaned_text.endswith('Java')}")

# 5. Replacing substrings using replace()
replaced_text = cleaned_text.replace("Python", "AI")
print(f"After replace():       '{replaced_text}'")

# 6. Counting occurrences using count()
letter_count = cleaned_text.lower().count("o")
print(f"Number of 'o's:        {letter_count}")

# 7. Checking character types using isdigit() and isalpha()
numeric_str = "2026"
alpha_str = "Python"
print(f"Is '{numeric_str}' all digits? {numeric_str.isdigit()}")
print(f"Is '{alpha_str}' all letters? {alpha_str.isalpha()}")
