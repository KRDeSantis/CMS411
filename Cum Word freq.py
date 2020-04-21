'''
This code was mainly written by Ethan Dyer.
This code looks at a folder specified by the path variable within the code for documents to summarize
the length of which can be controlled by the NUM_SENT variable. It also calculates how long it took to
summarize each of the documents.

One idea of fixing this summarizer is making it so that there is a better system of sorting than bubble sort
However this might not improve times that much
'''



# Packages
import docx2txt
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lemmatizer import Lemmatizer
from spacy.lookups import Lookups
from collections import defaultdict
import os
import glob
import time

#Start with a specific path from the current directory to the folder we have our input documents
path = './input/'
documents = 0
totalTime = 0
#For every document, start making a summary
for filename in glob.glob(os.path.join(path, '*.docx')):
    #Start a timer to help calculate how long it takes per document to summarize
    start = time.time() # start timer
    documents += 1
    document1 = docx2txt.process(filename)
    NUM_SENT=3 # number of sentences in summary

    #Stopwords are words that are so common that they add little to nothing to the information or context
    #of the speech. Removing these is as simple as making sure that we have a list of stop words,
    #and making sure they aren't in it.
    stopwords = list(STOP_WORDS)

    #The package of spacy to load. There are three flavors, _sm _md and _lg. The larger the package,
    #The more information that you will have, such as with similarity vectors and more words
    #being in the vocabulary. However, may take longer to load.
    nlp = spacy.load('en_core_web_md')
    
    #Send the document through the natural language processor. This is what does the assigning of 
    #Vectors, part of speech, everything.
    docx = nlp(document1)



    word_frequencies = {} # how many times each word occurs int the document
    words = [] # a list of every word in the document stores in the same index of the frequency array

    #spacy lemmatizer to get root words
    lookups = Lookups()
    lemmatizer = Lemmatizer(lookups)


    for word in docx: # go through every word in document
        if word.text not in stopwords: # as long as the word isnt a stop word
            if lemmatizer.lookup(word.text) not in word_frequencies.keys(): # if we havent come across the word yet
                word_frequencies[lemmatizer.lookup(word.text)] = 1 # its frequency is one
                words.append(lemmatizer.lookup(word.text)) # add it to words

            else:
                word_frequencies[lemmatizer.lookup(word.text)] += 1 # otherwise it is already in the list, so increment it


#Sort through the array by bubble sort
    def bubble_sort(arrNum, arrStr):
        def swapNum(i, j):
            arrNum[i], arrNum[j] = arrNum[j], arrNum[i]
        def swapStr(i, j):
            arrStr[i], arrStr[j] = arrStr[j], arrStr[i]
        n = len(arrNum)
        swapped = True

        x = -1
        #While the swapped condition is true, swap the sentences until it is in its right spot in the array
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

    #Make a variable that holds the string of what the end text will look like
    fileOutput = ''
    #the output folder for where we're going to put the summarized document
    outfold = ".//output//"
    #For each sentence in the summary, separate them and put them into a text file with sum_ to denote that it is, indeed, a summary
    for i in range(0, NUM_SENT):
        fileOutput += (str(sentenceList[i])) + '\n\n\n'
    #Get the filename of the summary
    fn =  filename[len(path):len(filename) - 4] + "txt"
    #Add a sum_ to the name to denote it being a summary, open a spot for writing into
    out = open(outfold + "sum_" + fn, 'w+')
    #Write our output
    out.write(fileOutput)
    #And close it to make sure there are no errors
    out.close()
    totalTime +=  time.time() - start

#How long was the entire summarization attempt? Put it in a document in the output folder
#and detail avg time per document and how long it took overall
totalTime = int(totalTime)
stats = open(outfold + "stats.txt", 'w+')
stats.write("total time : " + str(totalTime) + " seconds \n\n")
stats.write("documents processed : " + str(documents)+ "\n\n")
stats.write("average time per document : " + str(totalTime/documents) + " seconds \n\n")
stats.close()
















