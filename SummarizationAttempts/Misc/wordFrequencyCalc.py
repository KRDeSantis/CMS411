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

#change the text to whatever document you want to process.
document1 = docx2txt.process("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx")#### File location



stopwords = list(STOP_WORDS)

len(stopwords)

nlp = spacy.load('en_core_web_md')

docx = nlp(document1)

#Creates a list of non-stopwords and adds a counter for
#how often they occur in the document
word_frequencies = {}
for word in docx:
	if word.text not in stopwords:
		if word.text not in word_frequencies.keys():
			word_frequencies[word.text] = 1
		else:
			word_frequencies[word.text] += 1

# Maximum Frequency
maximum_frequency = max(word_frequencies.values())

#Lowest frequency gets compared against a decimal, 
#because word_frequencies[w]/maximum_frequency is the 
#proportion of the amount of times a specific word occurs
#compared against the most frequent word. This is why 
#lowest_freq is 1, because unless the document only has 
#one word repeated over and over, the word with the lowest
#frequency should be chosen
lowest_freq = 1
    
for w in word_frequencies:
    if (word_frequencies[w]/maximum_frequency) < lowest_freq:
        lowest_freq = word_frequencies[w]/maximum_frequency

#print normal word frequencies
for w in word_frequencies:
    print(w, word_frequencies[w])


#if the word frequency is greater than the least frequent 
#word or words, print out the word we're on in the loop
#and how often it occurs
"""
for w in word_frequencies:
    if (word_frequencies[w]/maximum_frequency) > lowest_freq:
       print(w, word_frequencies[w])
"""


