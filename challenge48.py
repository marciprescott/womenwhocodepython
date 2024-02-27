"""A program that replaces specific words in a text with their synonyms"""

import nltk
from nltk.corpus import wordnet
import random


# Input word to replace
# Output synonym of  word


synonyms = []
for syn in wordnet.synsets("love"):
    synonyms = []
    for l in syn.lemmas():
        synonyms.append(l.name())
print(set(synonyms))
