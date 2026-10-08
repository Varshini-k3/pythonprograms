# Program to calculate the volume and surface area of a cuboid

# Get dimensions from the user
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

# Formulas
surface_area = 2 * (length * width + width * height + height * length)
volume = length * width * height

# Display the results
print(f"Total Surface Area: {surface_area}")
print(f"Volume: {volume}")
