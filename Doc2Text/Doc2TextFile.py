# -*- coding: utf-8 -*-
#DeSantis Doc 2 Text #
# From Youtube tutorial #
# Created in Spyder #
import docx

#This function takes in a file name and reads it, returning the document.
#This file was mostly done to familiarize ourselves with the different text libraries that we could use
def ReadingTextDocuments(fileName):
    #Read in the document
    doc = docx.Document(fileName)
    
    # an array for holding the paragraphs
    completedText = []
    
    #For each paragraph in the document, add it as a new spot in the array 
    for paragraph in doc.paragraphs:
        completedText.append(paragraph.text)
        
    return '\n' .join(completedText)
    
    #Print out what we get from the file
print(ReadingTextDocuments('ReadInFile.docx'))
    
    


