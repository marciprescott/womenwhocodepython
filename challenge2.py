# Create a program to calculate the area of a circle given its radius.
# A = pi * r**2
# inputs = pi, radius of circle
# outputs = Area of a circle

pi = 3.14
radius = float(input("Enter radius of circle: "))


def calculate_area(pi, radius):
    return pi * radius**2


print(calculate_area(pi, radius))
