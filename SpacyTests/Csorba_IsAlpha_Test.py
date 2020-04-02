# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:24:01 2020

@author: Thomas Csorba

Trying to figure out some stuff relating to capitalization and the feasibility of using it
to help determine if it will work in our program
"""

import docx2txt
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

document1 = docx2txt.process("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx")#### File location

#document2 = #### File location

stopwords = list(STOP_WORDS)

len(stopwords)

nlp = spacy.load('en_core_web_md')

docx = nlp(document1)


importantWords = []
for word in docx:
	if word.text not in stopwords:
         if str(word)[0].isupper() == True:
             if str(word).lower() != "the":
                 if len(str(word)) > 2:
                     importantWords.append(word)
           
#for word in importantWords:
sentence_list = [sentence for sentence in docx]

print(importantWords)
