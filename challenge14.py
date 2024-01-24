# Using recursion which will take forever the larger the number becuase it is taking
# exponential time.
def fib_1(n):
    # Base cases
    if n <= 0:
        print("Please enter a number greater thatn 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_1(n - 2) + fib_1(n - 1)


print(fib_1(10))

# Write a program to avoid calculating the same functions over and over, write one that calculates
# the number in order until you reach the one you care about.


def fib_2(n):
    # Store first two steps in Fib in list
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[-2] + fib_list[-1])
        # Printing the list as we iterate to see the sequence
        print("the list now contains the following elements: ", fib_list)
    return fib_list[n]


print(fib_2(10))
