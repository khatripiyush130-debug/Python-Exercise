import math
def area_circle(radius):
    return math.pi * radius * radius
def area_rectangle(length, width):
    return length * width
print("Geometric Calculations")
print("1. Area of Circle")
print("2. Area of Rectangle")
choice = int(input("Enter your choice: "))
if choice == 1:
    radius = float(input("Enter radius: "))
    print("Area of Circle:", area_circle(radius))
elif choice == 2:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area of Rectangle:", area_rectangle(length, width))
else:
    print("Invalid choice")
