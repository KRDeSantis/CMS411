'''
Original Code Written by Ethan, with this test variant written by Thomas Csorba
This program was an attempt to incorporate searching for headings in the cumulative word frequency search
that we had already made. However, this went south as the approach wasn't as foolproof as initially thought.
For example, because of document formatting, finding bolding is not consistent. 
Runs, which hold slices of text from what MSWord considers a paragraph are supposed to have tags 
to show what is bolded and what is not. However, when using the docx functionality to
check runs for bolding, many things that actually were bolded in the document returned negative.
It wasn't until I was done making this that I figured this out, as the documents I was initially using to
debug finding these areas worked on those specific documents.

Another issue is that when applicable documents that the finding bolding works on are run through the 
summarizer, less important or coherent information is shown than if done without attempting to find specific
sections.




'''

# Packages
import docx2txt

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lemmatizer import Lemmatizer
from spacy.lookups import Lookups
from collections import defaultdict
from docx import Document
import os
import glob
import time
import re

#Start with a specific path from the current directory to the folder we have our input documents
path = './input/'
documents = 0
totalTime = 0
#For every document, find and make a summary of it.
for filename in glob.glob(os.path.join(path, '*.docx')):
    #Start a timer to help calculate how long it takes per document to summarize
    start = time.time() # start timer
    documents += 1


    '''
    The heading search has a list of words that it searches for the bolding of, and when it finds it,
    adds its sentence and all sentences until the next bolded section, which in most documents would 
    be a heading.
    
    '''
    def HeadingSearch(fileName):
        document = Document(fileName)
        finalString = []
        #List of terms that we found in headings in some of the documents given, and tried to use
        searchTerms = ["Summary", "Synopsis", "Conclusion", "Requirements", "Scope", "Background"]      
        #For each term, look for it in the bolded runs of each paragraph. If it can't be found, 
        #move on to the next word
        for headingTerm in searchTerms:
            breakOut = False
            boldingFound = False
            #Start splitting the document into MSWord paragraphs
            for paragraph in document.paragraphs:
                #If we found what we were looking for, break out of the loops and search for some other word
                if(breakOut):
                    break
                #Start splitting the paragraph into its runs
                for run in paragraph.runs:
                    #If we havent found bolding, then find the word we're looking for.
                    if(boldingFound == False):
                        requirementSearch = re.findall(headingTerm, run.text)
                        #If we return a result, and there was bolding there, then add the string to the list
                        if(run.bold and len(requirementSearch) >= 1):
                            finalString.append(run.text)
                            boldingFound = True
                    #if we reach the else statement, we've found bolding for the word, so if we find another run 
                    #That also has bolding, TYPICALLY then we've found another section and we stop.
                    else:
                        if(run.bold):
                            breakOut = True
                            break
                        #If we haven't found another bolded run, then add the string to what we're going to return
                        #to the summarizer
                        else:
                            finalString.append(run.text)
        #If we don't have enough sentences to make a summary, just do the normal summarization without
        #heading search
        if(len(finalString) <= 3):
            return False
        #If we do, return the sections that we've found that are relevant
        else:
            summaryString = "\n"
            summaryString = summaryString.join(finalString)
            print(summaryString)
            return summaryString

        

        
            
            

    
    NUM_SENT=3 # number of sentences in summary
    #stopwords is words that are so commonly used or too general that their impact on a sentence and meaning
    #is either negligible or negative.
    stopwords = list(STOP_WORDS)
    #The package of spacy to load. There are three flavors, _sm _md and _lg. The larger the package,
    #The more information that you will have, such as with similarity vectors and more words
    #being in the vocabulary
    nlp = spacy.load('en_core_web_md')
    docx = ""
    returnedSearch = HeadingSearch(filename)
    #If we didnt find anything with the heading search, just use the whole document.
    if(returnedSearch == False):
        document1 = docx2txt.process(filename)
        docx = nlp(document1)
        #Otherwise, send the headingsearch result through nlp
    else:
        docx = nlp(returnedSearch)

        
    



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
        #While the swapped condition is true, swap the sentences until it is in its right spot
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

    fileOutput = ''
    #the output folder for where we're going to put the summarized document
    outfold = ".//output//"
    #For each sentence in the summary, separate them and put them into a text file with sum_ to denote that it is, indeed, a summary
    for i in range(0, NUM_SENT):
        #Make the string readable before putting it in the document
        fileOutput += (str(sentenceList[i])) + '\n\n\n'
    fn =  filename[len(path):len(filename) - 4] + "txt"
    
    out = open(outfold + "sum_" + fn, 'w+')
    #Write the string that was made earlier
    out.write(fileOutput)
    #Close the file
    out.close()
    #Calculate how long the document took
    totalTime +=  time.time() - start

#How long was the entire summarization attempt? Put it in a document in the output folder
#and detail avg time per document and how long it took overall
totalTime = int(totalTime)
stats = open(outfold + "stats.txt", 'w+')
stats.write("total time : " + str(totalTime) + " seconds \n\n")
stats.write("documents processed : " + str(documents)+ "\n\n")
stats.write("average time per document : " + str(totalTime/documents) + " seconds \n\n")
stats.close()

















