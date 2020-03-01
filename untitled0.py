# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 18:18:04 2020

@author: TF-01
"""

import docx2txt

import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# change the text to whatever document you want to process.
document1 = docx2txt.process("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx")  #### File location

stopwords = list(STOP_WORDS)

len(stopwords)

nlp = spacy.load('en_core_web_md')

docx = nlp(document1)

print(stopwords)