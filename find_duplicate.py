
# Original list with duplicate elements
original_list = [10, 20, 10, 30, 20, 40, 10]

# Remove duplicates while maintaining order
unique_list = list(dict.fromkeys(original_list))

print("Ordered unique list:", unique_list)
# Output: [10, 20, 30, 40]
