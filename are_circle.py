#A Program to find area of circle

import math    #importing math bcz we use pie value

radius = float(input("Enter the radius of the circle: "))

#calculate the area of circle

area = math.pi*(radius**2)

print(f"The area of circle with radius {radius} is: {area}")

