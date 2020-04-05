# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:44:06 2020

@author: Kristen
https://medium.com/better-programming/extractive-text-summarization-using-spacy-in-python-88ab96d1fd97
"""
import spacy
from collections import Counter
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
import docx2txt

nlp = spacy.load("en_core_web_lg")
document = docx2txt.process("(Edited) 02 - DRAFT_6_SUAS_Engineering_Services_Sample_TO_08Nov19 (Task Order 0.docx")




def top_sentence(text, limit):
    keyword = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    doc = nlp(text.lower())
    for token in doc:
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            keyword.append(token.text)
    
    freq_word = Counter(keyword)
    max_freq = Counter(keyword).most_common(1)[0][1]
    for w in freq_word:
        freq_word[w] = (freq_word[w]/max_freq)
        
    sent_strength={}
    for sent in doc.sents:
        for word in sent:
            if word.text in freq_word.keys():
                if sent in sent_strength.keys():
                    sent_strength[sent]+=freq_word[word.text]
                else:
                    sent_strength[sent]=freq_word[word.text]
    
    summary = []
    
    sorted_x = sorted(sent_strength.items(), key=lambda kv: kv[1], reverse=True)
    
    counter = 0
    for i in range(len(sorted_x)):
        summary.append(str(sorted_x[i][0]).capitalize())

        counter += 1
        if(counter >= limit):
            break
            
    return ' '.join(summary)

print(top_sentence(document, 10))
