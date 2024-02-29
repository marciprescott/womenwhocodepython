"""A program that implements the bubble sort algorithm which is a sorting 
algorithm that starts from the first element of an array and 
ompares it with the second element. If the first element is 
greater than the second, we swap them. It continues this 
process until the end of the array, with the largest 
elements “bubbling” to the top."""

def bubble(list_a):
    # Can't perform comparision on last number of list so we use list - 1
    indexing_length = len(list_a) - 1
    # Use a sorted variable to break us out of the control flow once list has been sorted
    sorted = False
    # Perform a number of iterations we don't know how many so as long as sorted is False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            # Do comparision if value to left is greater than value to right
            if list_a[i] > list_a[i + 1]:
                sorted = False
                # Flip the items
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
                # When sorted is True we can stop the compare and break out of loop
    return list_a


print(bubble([127, 230, 288, 74, 148, 293, 293, 289, 243, 184]))
