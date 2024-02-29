import unittest


def is_anagram(s1, s2):
    """Checks if two strings are anagrams using sort

    Args:
        s1 (string):
        s2 (string):

    Returns:
        Boolean: True if anagrams, False otherwise
    """
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

def is_anagram_1(s, t):
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        # Count occurrences of character in stringS
        countS[s[i]] = countS.get(s[i], 0)
        # Count occurrences of character in stringT
        countT[t[i]] = countT.get(t[i], 0)

class TestIsAnagram(unittest.TestCase):

    def test_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("heart", "earth"))
        self.assertTrue(is_anagram("elvis", "lives"))
        self.assertTrue(is_anagram("bad credit", "debit card"))
        self.assertTrue(is_anagram("schoolmaster", "theclassroom"))

    def test_not_anagram(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("camp", "layabout"))
        self.assertFalse(is_anagram("dog", "doge"))
        self.assertFalse(is_anagram("Luna", "Duffy"))
        self.assertFalse(is_anagram("honey", "chile"))


if __name__ == "__main__":
    unittest.main()
