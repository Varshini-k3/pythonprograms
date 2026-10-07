# Define two matrices of the same shape (2x3)
matrix_a = [[1, 2, 3]]

matrix_b = [[7, 8, 9]]

# Initialize a result matrix with zeros (same shape: 2x3)
result = [[0 for _ in range(len(matrix_a[0]))] for _ in range(len(matrix_a))]

# Iterate through rows
for i in range(len(matrix_a)):
    # Iterate through columns
    for j in range(len(matrix_a[0])):
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]

print("Result using nested loops:")
for row in result:
    print(row)
