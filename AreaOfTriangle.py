import math

# Take input for the sides of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Calculate the semi-perimeter
s = (side1 + side2 + side3) / 2

# Calculate the area using Heron's formula
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

# Display the area of the triangle
print(f"The area of the triangle is {area}")