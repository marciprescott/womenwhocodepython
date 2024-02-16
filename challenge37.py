"""A program to iterate through a dictionary & print its keys and values"""

import unittest
from unittest.mock import patch
from io import StringIO


def dict_iterate(dict1):

    for key, value in dict1.items():
        print(f"{key}: {value}")


student_scores = {"Aly": 85, "Bo": 90, "Caysee": 78, "Duf": 82, "Eva": 95}
dict_iterate(student_scores)
