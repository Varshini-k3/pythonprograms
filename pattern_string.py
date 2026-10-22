# Take the number of rows as input from the user
num = int(input("Enter a number to generate its pattern: "))

# Outer loop to handle the number of rows
for i in range(1, num + 1):
    # Inner loop to print numbers in each row
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Move to the next line after completing a row
    print()
