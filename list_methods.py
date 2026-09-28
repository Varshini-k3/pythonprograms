# Python List Methods

numbers = [10, 20, 30, 40]

print("Original list:", numbers)

# 1. append()
numbers.append(50)
print("After append(50):", numbers)

# 2. insert()
numbers.insert(1, 15)
print("After insert(1, 15):", numbers)

# 3. remove()
numbers.remove(30)
print("After remove(30):", numbers)

# 4. pop()
numbers.pop()
print("After pop():", numbers)

# 5. index()
position = numbers.index(20)
print("Index of 20:", position)

# 6. count()
numbers.append(20)
print("After adding another 20:", numbers)
print("Count of 20:", numbers.count(20))

# 7. sort()
numbers.sort()
print("After sort():", numbers)

# 8. reverse()
numbers.reverse()
print("After reverse():", numbers)

# 9. copy()
new_list = numbers.copy()
print("Copied list:", new_list)

# 10. clear()
numbers.clear()
print("After clear():", numbers)
