list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find union using set().union()
union_list = list(set(list1).union(list2))

print("Union of lists:", union_list)
# Output: [1, 2, 3, 4, 5, 6, 7, 8] (Order may vary)
