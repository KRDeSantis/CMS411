# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:24:01 2020

@author: Thomas Csorba

Trying to figure out some stuff relating to capitalization and the feasibility of using it
to help determine if it will work in our program


The usability seems to be limited insofar as it is too vague. While in conjunction with another form of
search it may work, as most words that are capitalized are the requesting entities, the headings in a 
specific section, among other things.
"""

import docx2txt
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

#The name of the file we wish to process
document1 = docx2txt.process("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx")


stopwords = list(STOP_WORDS)

len(stopwords)

#Load the medium spacy package so there is at least vectors for calculating similarity
nlp = spacy.load('en_core_web_md')

docx = nlp(document1)

#An array that will hold the important words, IE those capitalized
importantWords = []
for word in docx:
	if word.text not in stopwords:
         if str(word)[0].isupper() == True:
             #The is a common capitalized word, so we ignore it. Could alternatively add it to stopwords
             if str(word).lower() != "the":
                 if len(str(word)) > 2:
                     importantWords.append(word)
           
#Print the sentences in the document
sentence_list = [sentence for sentence in docx]

print(sentence_list + "\n")

print("\n \n " + importantWords)
