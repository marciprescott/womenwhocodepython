import math

p = 10.1
print(math.ceil(p))  # 11
print(math.pi)  # 3.141592653589793


def circle_area(r):
    return math.pi * r**2


radius = 3

print("Area =", circle_area(radius))  # Area = 28.274333882308138

print(math.tau)  # 6.283185307179586

print(math.e)  # 2.718281828459045

print(math.nan)  # nan

print(type(math.nan))  # <class 'float'>

print(math.inf)  # inf

print(-math.inf)  # -inf

q = 9.99
print(math.floor(q))  # 9

n = 5
print("{}! = {}".format(n, math.factorial(n)))  # 5! = 120

gcd = math.gcd(25, 120)
print(gcd)  # 5

print(math.fabs(-25))  # 25.0

# math.pow(x,y) returns a floating point value rep the value of x** y
deposit = 10000
interest_rate = 0.04
number_years = 5
final_amount = deposit * math.pow(1 + interest_rate, number_years)
print(
    "The final amount after five years is", final_amount
)  # The final amount after five years is 12166.529024000001
print(type(math.pow(2, 4)))  # <class 'float'>

print(math.sqrt(16))  # 4.0

print(math.log(10))  # 2.302585092994046 natural logarithm of 10
print(math.log(10, 3))  # 2.095903274289385 logarithm 10 to base 3

# Hyperbolic Functions
x = 0.5
print(math.cosh(x))  # 1.1276259652063807
print(math.sinh(x))  # 0.5210953054937474
print(math.tanh(x))  # 0.46211715726000974
