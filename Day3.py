# CODE
print("1] Area of Triangle\n2] Area of Rectangle\n3] Area of Square")
z = int(input("Enter choice: "))

if z == 1:
    a = int(input("Height of triangle: "))
    b = int(input("Base of triangle: "))
    a = (0.5)*a*b
    print("Area of triangle is: ", a)

elif z == 2:
    a = int(input("Length of rectangle: "))
    b = int(input("Breadth of rectangle: "))
    a = a*b
    print("Area of rectangle is: ", a)

elif z == 3:
    a = int(input("Side of Square: "))
    a = a**2
    print("Area of square is: ", a)

else:
    print("Enter correct choice.")
  


# INPUTS and OUTPUT


# a)Triangle
#1] Area of Triangle
#2] Area of Rectangle
#3] Area of Square
#Enter Choice: 1
#Height of triangle: 15
#Base of triangle: 5
#Area of triangle is: 37.5
	
# b)Rectangle
#1] Area of Triangle
#2] Area of Rectangle
#3] Area of Square
#Enter Choice: 2
#Length of rectangle: 10
#Breadth of rectangle: 5
#Area of rectangle is: 50

# c)Square
#1] Area of Triangle
#2] Area of Rectangle
#3] Area of Square
#Enter Choice: 3
#Side of Square: 4
#Area of aquare is: 16
