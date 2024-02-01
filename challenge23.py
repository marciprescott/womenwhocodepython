""" A program that checks if a key exists in a dictionary."""

dic = {"x": 100, "y": 200, "z": 300}


def does_key_exist(key):
    if dic.get(key) == None:
        print("The key you entered IS NOT in the dictionary!")
    else:
        print("The ke you entered IS in the dictionary!")


key = input("Enter key to verify existence: ")

does_key_exist(key)
