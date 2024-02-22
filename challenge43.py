"""A program that removes all whitespaces from a given string"""


def remove_whitespaces(txt):
    return txt.replace(" ", "")


txt = input("Enter string you would like to remove whitespaces from: ")
print(remove_whitespaces(txt))


def test_remove_whitespaces():
    # Test case 1: Input with spaces
    assert remove_whitespaces("hello world") == "helloworld"

    # Test case 2: Input with tabs
    assert remove_whitespaces("hello\tworld") == "hello\tworld"

    # Test case 3: Input with newlines
    assert remove_whitespaces("hello\nworld") == "hello\nworld"

    # Test case 4: Input with mixed whitespace characters
    assert remove_whitespaces("hello  \t\nworld") == "hello\t\nworld"

    # Test case 5: Empty input
    assert remove_whitespaces("") == ""

    # Test case 6: Input with leading and trailing whitespace
    assert remove_whitespaces("  hello world  ") == "helloworld"

    # Test case 7: Input with only whitespace characters
    assert remove_whitespaces("    ") == ""

    print("All tests passed!")


# Run the test
test_remove_whitespaces()
