"""A program that replaces specific words in a text with their synonyms"""

import nltk
import random
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize


def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return set(synonyms)  #  Convert to set


def replace_with_synonyms(text, words_to_replace):
    for word in words_to_replace:
        synonyms = get_synonyms(word.lower())
        if synonyms:
            text = text.replace(word, random.choice(list(synonyms)))
        return text


text = "Learning to code is hard, I put quite a bit of time into the process."

words_to_replace = {"hard"}
replaced_text = replace_with_synonyms(text, words_to_replace)
print("Original text:", text)
print("Text with synonyms replaced:", replaced_text)

# Result  = Original text: Learning to code is hard, I put quite a bit of time into the process.
# Text with synonyms replaced: Learning to code is backbreaking, I put quite a bit of time into the process.
