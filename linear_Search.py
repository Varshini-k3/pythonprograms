def linear_search(items, key):
    """
    Searches for a key in a list using linear search.
    Returns the index if found, or -1 if not found.
    """
    # Loop through every element in the list with its index
    for index in range(len(items)):
        if items[index] == key:
            return index  # Target found, return the current location
            
    return -1  # Target not found after checking the whole list

# Example usage:
numbers = [42, 7, 19, 88, 23, 11]
target_key = 23

# Run the search
result_index = linear_search(numbers, target_key)

# Display the results
if result_index != -1:
    print(f"Key {target_key} found at index location: {result_index}")
else:
    print(f"Key {target_key} was not found in the list.")
