# CODE
import math

print("1] Volume of sphere\n2] Volume of cylinder")
z = int(input("Enter choice: "))

if z == 1:
    a = float(input("Input radius:"))
    vol = (4/3)*math.pi*(a**3)
    print("Volume of sphere is: ", round(vol, 3))

elif z == 2:
    a = float(input("Radius of base: "))
    b = float(input("Height of cylinder: "))
    a = math.pi*(a**2)*b
    print("Volume of Cylinder is: ", round(a, 3))


# INPUTS and OUTPUT

#	a) Sphere
# 1] Volume of sphere
# 2] Volume of cylinder
# Enter choice: 1
# Input radius: 5
# Volume of sphere is: 523.598

#	b) Cylinder
# 1] Volume of sphere
# 2] Volume of cylinder
# Enter choice: 2
# Radius of base: 5
# Height of cylineder: 10
# Volume of Cylinder is: 785.398
