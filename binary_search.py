def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    # Keep searching while the search space is valid
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            low = mid + 1
            
        # If target is smaller, ignore the right half
        else:
            high = mid - 1
            
    # Target was not present in the list
    return -1

# Example usage:
# Crucial Requirement: The input list MUST be sorted.
sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_val = 23

result = binary_search(sorted_list, target_val)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
