# -*- coding: utf-8 -*-
#DeSantis Doc 2 Text #
# From Youtube tutorial #
# Created in Spyder #
import docx

def ReadingTextDocuments(fileName):
    doc = docx.Document(fileName)
    
    completedText = []
    
    for paragraph in doc.paragraphs:
        completedText.append(paragraph.text)
        
        return '\n' .join(completedText)
    
    
print(ReadingTextDocuments('ReadInFile.docx'))
    
    

