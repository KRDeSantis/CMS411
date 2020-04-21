'''
Ask Ethan if he wants this deleted
Looks exactly the same as the working one just without folder stuff
'''



# Packages
import docx2txt

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lemmatizer import Lemmatizer
from spacy.lookups import Lookups
from collections import defaultdict



inputDoc = "test1.docx" #### File location
document1 = docx2txt.process(inputDoc)
NUM_SENT=3 # number of sentences in summary

stopwords = list(STOP_WORDS)

nlp = spacy.load('en_core_web_md')
docx = nlp(document1)



word_frequencies = {} # how many times each word occurs int the document
words = [] # a list of every word in the document stores in the same index of the frequency array

#spacy lemmatizer to get root words
lookups = Lookups()
lemmatizer = Lemmatizer(lookups)


for word in docx: # go thorough every word in document
    if word.text not in stopwords: # as long as the word isnt a stop word
        if lemmatizer.lookup(word.text) not in word_frequencies.keys(): # if we havent come across the word yet
            word_frequencies[lemmatizer.lookup(word.text)] = 1 # its frequency is one
            words.append(lemmatizer.lookup(word.text)) # add it to words

        else:
            word_frequencies[lemmatizer.lookup(word.text)] += 1 # otherwise it is already in the list, so increment it



def bubble_sort(arrNum, arrStr):
    def swapNum(i, j):
        arrNum[i], arrNum[j] = arrNum[j], arrNum[i]
    def swapStr(i, j):
        arrStr[i], arrStr[j] = arrStr[j], arrStr[i]
    n = len(arrNum)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arrNum[i - 1] < arrNum[i]:
                swapNum(i - 1, i)
                swapStr(i - 1, i)
                swapped = True



    return arrStr


sentenceList = [] # list of the sentences
topTotals = [] # list of average word frequencies per sentence



for sent in docx.sents:
    sentenceTotal = 0 #cumulative frequency of words in sentence
    for word in sent:
        sentenceTotal += word_frequencies.get(lemmatizer.lookup(word.text),0) #add the frequency of the current word
    topTotals.append(sentenceTotal) # add cumulative word frequency to list
    sentenceList.append(sent) # add sentence to list
sentenceList = bubble_sort(topTotals, sentenceList) # sort sentence list based on cumulative frequency list



# print number of sentences specified
for i in range(0,NUM_SENT):
    print(str(sentenceList[i]))














