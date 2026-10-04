# Prompt the user for input and convert to float
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area
area = 0.5 * base * height

# Display the result (rounded to 2 decimal places)
print(f"The area of the triangle is: {area:.2f}")
