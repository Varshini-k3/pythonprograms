# Step 1: Get 3 numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Step 2: Find the largest number
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

# Step 3: Find the smallest number
if (num1 <= num2) and (num1 <= num3):
    smallest = num1
elif (num2 <= num1) and (num2 <= num3):
    smallest = num2
else:
    smallest = num3

# Step 4: Print the results
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
