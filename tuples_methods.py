# 1. Initialize a tuple containing duplicate values
numbers_tuple = (10, 20, 30, 40, 20, 50, 20)
print(f"Original Tuple: {numbers_tuple}")

# 2. Implement the count() method
# Returns the total number of times a specified value appears in the tuple
count_of_20 = numbers_tuple.count(20)
print(f"\n--- Method: count() ---")
print(f"The number 20 appears {count_of_20} times in the tuple.")

# 3. Implement the index() method
# Finds the first occurrence of a specified value and returns its position (0-indexed)
index_of_30 = numbers_tuple.index(30)
index_of_20 = numbers_tuple.index(20) # Finds the very first '20'

print(f"\n--- Method: index() ---")
print(f"The first occurrence of 30 is at index: {index_of_30}")
print(f"The first occurrence of 20 is at index: {index_of_20}")

# 4. Demonstrating Built-in Functions commonly used with tuples
print(f"\n--- Useful Built-in Functions ---")
print(f"Total elements (len): {len(numbers_tuple)}")
print(f"Maximum value (max): {max(numbers_tuple)}")
print(f"Minimum value (min): {min(numbers_tuple)}")
