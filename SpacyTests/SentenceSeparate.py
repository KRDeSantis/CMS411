#Separating sentences#
#Kelley DeSantis#
"""
This program was initially created to test splitting sentences into parts using docx2txt
Not much more to say, as it's just to test things.
"""

#import packages#
import spacy
import docx2txt

#Document to read in #
document1 = docx2txt.process("ReadInFile.docx")
#Since we're just testing, load in the smallest spacy package
nlp = spacy.load("en_core_web_sm")
doc = nlp(document1)

#separate the sentence and print out each of them
for sent in doc.sents:
    print(sent.text)
