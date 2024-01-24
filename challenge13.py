# Write a program to shuffle the elements of a list randomly
# Inputs a list
# Ouputs a shuffled list

from random import randint


# Function to generate a random arrangement of the list
def custom_shuffle(input_list):
    # i > 0 since we don't need to run the first element
    # Start from the end of the input_list and swap
    for i in range(len(input_list) - 1, 0, -1):
        # Select the random index from 0 to i
        j = randint(0, i + 1)

        # Swap input_list[i] with element at random index
        input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list


input_list = list((5, 6, 7, 8, 1, 2, 3, 4))
print(custom_shuffle(input_list))
