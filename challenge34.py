""" A Python program to merge two dictionaries. 
There are several ways to do this: using update(), 
dict constructor, using merge | operator...  """


def merge_dicts_1(dict1, dict2):
    """
    Merge two dictionaries using "|" operator.

    Args:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.

    Returns:
    dict: The merged dictionary.
    """
    # Use “|” operator to merge two dictionaries
    result = dict1 | dict2
    return result


# Example usage
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = merge_dicts_1(dict1, dict2)
print("Merged dictionary:", merged_dict)

""" Test for accuracy. """
expected_result = {"a": 1, "b": 2, "c": 3, "d": 4}

# Test the merge_dicts function
result = merge_dicts_1(dict1, dict2)

# Check if the result matches the expected result
if result == expected_result:
    print("Test passed: dictionaries merged successfully.")
else:
    print("Test failed: dictionaries did not merge correctly.")
    print("Expected result:", expected_result)
    print("Actual result:", result)


def merge_dicts_2(d1, d2):
    """
    Merge two dictionaries using dict constructor.

    Args:
    d1 (dict): The first dictionary.
    d2 (dict): The second dictionary.

    Returns:
    dict: The merged dictionary.
    """
    # Create a copy of the first dictionary
    merged_dict = d1.copy()
    # Update the copy with the second dictionary
    merged_dict.update(d2)
    # Return the merged dictionary
    return merged_dict


d1 = {"I": 1, "did": 2, "Code": 5}
d2 = {"enjoy": 3, "this": 4, "project": 6}
d3 = merge_dicts_2(d1, d2)
print("The new dictionary is: ", d3)
