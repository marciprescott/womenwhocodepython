x = int(input("Enter the value of variable 'x': "))
y = int(input("Enter the value of variable 'y': "))
# assign old value of x to temp var
temp = x
print("old x is: ", temp)
# assign x to y
x = y
# assign y to temp or old value of x
y = temp

print("y is now: ", y)
print("x is now: ", x)
