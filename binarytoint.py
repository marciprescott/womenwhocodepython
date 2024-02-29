# binary_num = input("Enter binary number to convert: ")
# Removee the 0b prefix from the binary number string
binary_num = "0b1011"
binary_number = binary_num[2:]
print(binary_number)
# Nov reverse the number so we can iterate right to left
"""In this particular example, the slice statement [::-1] means 
start at the end
of the string and end at position 0,
move with the step 
-1, negative one, which means o
ne step backwards."""
binary_number = binary_number[::-1]
decimal_number = 0
# Iterate through each digit in the reversed binary string
for i in range(len(binary_number)):
    digit = int(binary_number[i])
    power = 2**i
    result = digit * power
    # Add result to the decimal number
    decimal_number += result
print(decimal_number)

from functools import reduce

binary = input("Enter a binary number: ")
decimal = reduce(lambda x, y: 2 * x + y, map(int, binary))
print("Decimal equivalent of ", binary, "is", decimal)
