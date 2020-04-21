# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:44:06 2020

@author: Thomas
https://medium.com/better-programming/extractive-text-summarization-using-spacy-in-python-88ab96d1fd97
This is the summarizer found on medium.com. While one of the better summarizers, it still
can provide less than coherent sentences. However, there are a few things that are done better, and
might be encouraged to be checked out in future iterations
"""
import spacy
from collections import Counter
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
import docx2txt

#Load larger nlp library, just to make sure that all the vectors and words are understood by the program
nlp = spacy.load("en_core_web_lg")
#The document to process goes in here.
document = docx2txt.process("(Edited) 02 - DRAFT_6_SUAS_Engineering_Services_Sample_TO_08Nov19 (Task Order 0.docx")



#The function that determines whether or not a sentence is valuable for use in a summary. It 
#Checks the frequency of the word, (as long as it has the part of speech desired or is not a stopword)
#and sentences with words that are very frequent are chosen.
'''
The first parameter is the text that the user wants to input, and the second is the maximum amount
of sentences the user wants returned.
'''
def top_sentence(text, limit):
    #Keywords in this instance is simply just the form of showing how often this word appears
    keyword = []
    #The position tag is used to check what type of word it is (part of speech wise), and this is
    #relevant to cutting out unimportant words for calculating the strength of a sentence
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    #look at the lowercase form of the word so that we can easier check it against spacy's library
    doc = nlp(text.lower())
    for token in doc:
        #If the text is in stopwords, which are words that are so common that they essentially add nothing
        #to the information of the text, or if the token is just punctuation, move to the next word
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        #If we find a word that doesn't match the previous if statement, then we check if it has
        #the part of speech tag that matches the ones we chose. If so, add it to our keywords.
        if(token.pos_ in pos_tag):
            keyword.append(token.text)
    
    #This section of the code normalizes the frequency of each word in relation to the most frequent word
    freq_word = Counter(keyword)
    max_freq = Counter(keyword).most_common(1)[0][1]
    for w in freq_word:
        freq_word[w] = (freq_word[w]/max_freq)
        
    #The strength of each sentence is then calculated by adding up the frequency of all the keywords in the
    #sentence. 
    sent_strength={}
    for sent in doc.sents:
        for word in sent:
            #if the word is in our keys, and we have that sentence in our sent_strength
            #then we want to add the word frequency to the sentence strength
            #if the sentence isn't there, then we add it to our sent_strength while also
            #making its value the same as the word frequency
            if word.text in freq_word.keys():
                #
                if sent in sent_strength.keys():
                    sent_strength[sent]+=freq_word[word.text]
                else:
                    sent_strength[sent]=freq_word[word.text]
    
    summary = []
    
    #Sort the sentences based on the normalized value. Reverse makes it so that it sorts the sentences by
    #how they ought to appear in relation to the document
    sorted_x = sorted(sent_strength.items(), key=lambda kv: kv[1], reverse=True)
    
    counter = 0
    for i in range(len(sorted_x)):
        #Make the first letter of the first sentence capitalized again
        summary.append(str(sorted_x[i][0]).capitalize())

        counter += 1
        #If we reached the amount of sentences we want to return, stop creating the summary
        if(counter >= limit):
            break
    #Return the summary to the caller
    return ' '.join(summary)

print(top_sentence(document, 10))
