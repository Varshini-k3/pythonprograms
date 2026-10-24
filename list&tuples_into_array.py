import array

# Define a standard Python list and tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = (6, 7, 8, 9, 10)

# Convert using type code 'i' (signed integer)
array_from_list = array.array('i', my_list)
array_from_tuple = array.array('i', my_tuple)

# Display results and verify data types
print("Built-in Array from List:", array_from_list)
print("Built-in Array from Tuple:", array_from_tuple)
