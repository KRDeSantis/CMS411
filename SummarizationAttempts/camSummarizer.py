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

#The name of the file we wish to process
document1 = docx2txt.process("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx")

#document2 = #### File location

#Stopwords are words that are so common they add no information to a sentence, so we ignore them
stopwords = list(STOP_WORDS)

len(stopwords)

#Spacy has small medium and large packages, which determine the amount of data for similarity vectors
#and information on part of speech. Larger packages may also take longer to load
nlp = spacy.load('en_core_web_md')

#Send the document through the NLP so that its words can be assigned their vectors, part of speech, etc.
docx = nlp(document1)

#Each word that isnt a stopword gets added to the word frequencies table, or has its occurence increased
#These word frequencies are used in determining sentence strength
word_frequencies = {}
for word in docx:
    if word.text not in stopwords:
        if word.is_oov is False:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

#Gets the value of the most frequent word
maximum_frequency = max(word_frequencies.values())

#The value of the most frequent word is used to normalize the frequency of all the words in 
#the word frequencies dictionary
for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)


#### Sentence Tokenization
#### scoring every sentence based on number of words
#### non-stopwords in our word frequency table

sentence_list = [ sentence for sentence in docx.sents ]

#Using the normalized word frequencies, we calculate the sentence scores by adding up all the 
#values of the words in the sentences
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

#Return the sentences with the highest values
summarized_sentences = nlargest(7,sentence_scores,key=sentence_scores.get)

#### Convert from spacy span to string
final_sentences = [ w.text for w in summarized_sentences ]

#### Join sentences
summary = ' '.join(final_sentences)

print(summary)
