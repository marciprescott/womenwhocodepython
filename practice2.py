import string


def print_rangoli(size):
    width = (size - 1) * 4 + 1
    alphabets = string.ascii_lowercase[:size]

    for i in range(size - 1, -size, -1):
        chars = "-".join(alphabets[size - 1 : abs(i) : -1] + alphabets[abs(i) : size])
        line = chars.center(width, "-")
        print(line)


# Example usage
if __name__ == "__main__":
    size = int(input("Enter the size of the alphabet rangoli: "))
    print_rangoli(size)
