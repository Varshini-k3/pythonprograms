def is_palindrome(text):
    # Convert to lowercase to ensure the check is case-insensitive
    cleaned_text = text.lower()
    
    # Compare the string with its reverse
    return cleaned_text == cleaned_text[::-1]

# Test the program
word = input("Enter a word to check: ")

if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
