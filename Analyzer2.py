# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 18:20:04 2020
@author: Thomas Csorba, Ethan Dyer
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
document1 = docx2txt.process("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx")  #### File location

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


limit =1 # words can only appear limit times. (reverse document frequency)

# find all words that appear limit times or less and put them into a list
lowest_freq =[]
for w in word_frequencies:
    if (word_frequencies[w] ) <= limit:
        lowest_freq.append(w)

sentenceList = []#sentences that will be outputted
keyWords= ["Scope", "Background", "Contract", "Contractor",
           "Requirements", "Summary", "Synopsis", "Conclusion"]# current list of keyWords
reasonList = [] # reason a sentence was chosen

# for every sentence
for sent in docx.sents:
    breakFlag = False # break flag to get out of loops if sentence is already chosen
    for word in sent:# for every word in that sentence
        if(breakFlag):
           break
        for w in lowest_freq:# for every word less that occurs limit times or less
            if(breakFlag):
                break
            if(str(word) == w):# does the word equal the current lowest freq word
                sentenceList.append(sent)#if so add the sentence
                reasonList.append(w + ":" + str(word_frequencies[w]))# and put w as the reason
                breakFlag = True# go to next sentence
        for key in keyWords:# go through all keywords
            if(breakFlag):
                break
            if(str(word)==key):# see if key is current word
                sentenceList.append(sent)# if so add the sentence
                reasonList.append(key)# the key is the reason
                breakFlag = True# go to next sentence 


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
