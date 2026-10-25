def first_non_repeating_char(s: str):
    # Step 1: Build the frequency map
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        
    # Step 2: Find the first character with a frequency of 1
    for char in s:
        if char_count[char] == 1:
            return char
            
    # Return None (or a specific placeholder like '_') if all characters repeat
    return None

# --- Test Cases ---
print(first_non_repeating_char("geeksforgeeks"))  # Output: f
print(first_non_repeating_char("racecar"))        # Output: e
print(first_non_repeating_char("aabbcc"))         # Output: None
