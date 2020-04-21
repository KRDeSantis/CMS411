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
#Don't forget to include directory if not in the same location as this python file
document1 = docx2txt.process("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx")  #### File location

#Stopwords are words that are so common that they add little to nothing to the information or context
#of the speech. Removing these is as simple as making sure that we have a list of stop words,
#and making sure they aren't in it.
stopwords = list(STOP_WORDS)

len(stopwords)

#Spacy library of words you want to load. Comes in sm md and lg.
#The larger the library, the more words they have metrics for when it comes to similarity and
#definition of part of speech, but can increase load times.
nlp = spacy.load('en_core_web_md')

docx = nlp(document1)

# Creates a list of non-stopwords and adds a counter for
# how often they occur in the document
word_frequencies = {}

#For each word in the document, if the lemmatized version of the
#word is not in the stop words and isn't out of vector 
#(meaning that it has vector values for helping determine word similarity)
#then we add it to our dictionary if it isn't there and assign it a value of one. Otherwise, add one to it.
for word in docx:    
    if word.lemma_ not in stopwords and word.is_oov == False:
        if word.text not in word_frequencies.keys():
            word_frequencies[word.text] = 1
        else:
            word_frequencies[word.text] += 1

#For the next part, a word is added to a list if it occurs limit times or less
limit = 3 
#Find the words
lowest_freq =[]
for w in word_frequencies:
    if (word_frequencies[w] ) <= limit:
        lowest_freq.append(w)

sentenceList = []#sentences that will be output
#List of keywords chosen to help choose sentences. These keywords were chosen as they appeared often and
#Seemed to provide relevant context to 
keyWords= [nlp("Scope"), nlp("Background"), nlp("Contract"), nlp("Contractor"),
           nlp("Requirements"), nlp("Summary"), nlp("Synopsis"), nlp("Conclusion")]# current list of keyWords
reasonList = [] # reason a sentence was chosen


input("To start lowest frequency search, press any key")

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
                reasonList.append(w + ": " + str(word_frequencies[w]))# and put w as the reason
                breakFlag = True# go to next sentence, even if there is another low frequency word
            
#print out the sentence and reason lists. These are used to try to understand why
#The summary outputs what it does.
for sent, reason in zip(sentenceList, reasonList):
    print(str(sent) + "\n" + reason + "\n\n")                
             
#Clear sentence and reason lists
sentenceList *= 0
reasonList *= 0    
    
input("To start keyword finding, press any key")               
                
                
for sent in docx.sents:
    breakFlag = False # break flag to get out of loops if sentence is already chosen
    for word in sent:# for every word in that sentence
        if(breakFlag):
           break                
        for key in keyWords:# go through all keywords
            if(breakFlag):
                break
            for token in key:                     
                #if the word has vector representation and the word that we're looking at is similar to the key we're looking at
                #append to our sentence and reason list
                if(word.has_vector == True and key.similarity(word) >= .7):# see if key is similar to current word if in vocab
                    sentenceList.append(sent)# if so add the sentence
                    reasonList.append(str(key))# the key is the reason
                    breakFlag = True# go to next sentence 


# print normal word frequencies
for sent, reason in zip(sentenceList, reasonList):
    print(str(sent) + "\n" + reason + "\n\n")


# if the word frequency is greater than the least frequent
# word or words, print out the word we're on in the loop
# and how often it occurs

