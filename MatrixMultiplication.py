# Define two matrices
matrix_a = [[12, 7, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_b = [[5, 8, 1, 2],
            [6, 7, 3, 0],
            [4, 5, 9, 1]]

# Initialize a result matrix with zeros 
# Dimensions will be (rows of A) x (columns of B) -> 3x4
result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]

# Iterate through rows of matrix_a
for i in range(len(matrix_a)):
    # Iterate through columns of matrix_b
    for j in range(len(matrix_b[0])):
        # Iterate through rows of matrix_b
        for k in range(len(matrix_b)):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]

print("Result using nested loops:")
for row in result:
    print(row)
