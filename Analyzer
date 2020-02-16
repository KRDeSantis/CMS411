# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 18:20:04 2020
@author: Thomas Csorba
Commented and edited version of the summarizer cam found
This version specifically checks for words that occur more
frequently than the least frequently used word or words
"""

# From YouTube tutorial: https://www.youtube.com/watch?v=XcZGKAF5zxg
# Packages
import docx2txt

import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# change the text to whatever document you want to process.
document1 = docx2txt.process("test1.docx")  #### File location

stopwords = list(STOP_WORDS)

len(stopwords)

nlp = spacy.load('en_core_web_md')

docx = nlp(document1)

# Creates a list of non-stopwords and adds a counter for
# how often they occur in the document
word_frequencies = {}


for word in docx:
    if word.text not in stopwords:
        if word.text not in word_frequencies.keys():
            word_frequencies[word.text] = 1
        else:
            word_frequencies[word.text] += 1

# Maximum Frequency
maximum_frequency = max(word_frequencies.values())

# Lowest frequency gets compared against a decimal,
# because word_frequencies[w]/maximum_frequency is the
# proportion of the amount of times a specific word occurs
# compared against the most frequent word. This is why
# lowest_freq is 1, because unless the document only has
# one word repeated over and over, the word with the lowest
# frequency should be chosen
limit =0

lowest_freq =[]
for w in word_frequencies:
    if (word_frequencies[w] ) <= limit:
        lowest_freq.append(w)

sentenceList = []
keyWords= ["Scope", "Background", "Contract", "Contractor",
           "Requirements", "Summary", "Synopsis", "Conclusion",
           "Performance Work Statement "]
reasonList = [];

for sent in docx.sents:
    breakFlag = False
    for word in sent:
        if(breakFlag):
           break
        for w in word_frequencies:
            if(breakFlag):
                break
            if(w == str(word)):
                sentenceList.append(sent)
                reasonList.append(w + ":" + str(word_frequencies[w]))
                breakFlag = True
        for key in keyWords:
            if(breakFlag):
                break
            if(str(word) == key):
                sentenceList.append(sent)
                reasonList.append(key)
                breakFlag = True


# print normal word frequencies
for sent, reason in zip(sentenceList, reasonList):
    print(str(sent) + "\n" + reason + "\n\n")


# if the word frequency is greater than the least frequent
# word or words, print out the word we're on in the loop
# and how often it occurs
"""
for w in word_frequencies:
    if (word_frequencies[w]/maximum_frequency) > lowest_freq:
       print(w, word_frequencies[w])
"""
