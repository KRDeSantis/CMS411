# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:20:04 2020

@author: Thomas Csorba
Copy of code
"""

# From YouTube tutorial: https://www.youtube.com/watch?v=XcZGKAF5zxg
# Packages
import docx2txt
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

document1 = docx2txt.process("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx")#### File location

#document2 = #### File location

stopwords = list(STOP_WORDS)

len(stopwords)

nlp = spacy.load('en_core_web_md')

docx = nlp(document1)

# Print out
#for token in docx:
#	print(token.text)

# Word Frequency Table
word_frequencies = {}
for word in docx:
    if word.text not in stopwords:
        if word.is_oov is False:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

# Maximum Frequency
maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)


#### Sentence Tokenization
#### scoring every sentence based on number of words
#### non-stopwords in our word frequency table

sentence_list = [ sentence for sentence in docx.sents ]

sentence_scores = {}
for sent in sentence_list:
	for word in sent:
		if word.text.lower() in word_frequencies.keys():
			if len(sent.text.split(' ')) < 30:
				if sent not in sentence_scores.keys():
					sentence_scores[sent] = word_frequencies[word.text.lower()]
				else:
					sentence_scores[sent] += word_frequencies[word.text.lower()]

from heapq import nlargest

summarized_sentences = nlargest(7,sentence_scores,key=sentence_scores.get)

#### Convert from spacy span to string

final_sentences = [ w.text for w in summarized_sentences ]

#### Join sentences

summary = ' '.join(final_sentences)

print(summary)
