# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 12:07:55 2020

@author: Thomas Csorba

Turn a docx file into a stream of XML information. This might help find the structure of the
word document, and in turn, allow for extraction of relevant data.
This requires the module zipfile to work
"""

import zipfile
import xml.dom.minidom
from spacy.lang.en.stop_words import STOP_WORDS

#All word documents are essentially zipfiles with XML describing how they're formatted.
#This takes the docx file and opens it like a zip file, and extracts the xml
document = zipfile.ZipFile("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx")

#This reads the document like a string
docString = document.read("word/document.xml")
#This array is for when we later split sentences by certain parts to help make it look clean
docXArr = []
Sent = str(docString)
docXArr = Sent.split("<w")

#Print each "sentence" in the array of split sentences
for sent in docXArr:
    print(sent + "\n")


'''
https://towardsdatascience.com/how-to-extract-data-from-ms-word-documents-using-python-ed3fbb48c122
https://gist.github.com/etienned/7539105
http://www.ecma-international.org/news/TC45_current_work/Office%20Open%20XML%20Part%204%20-%20Markup%20Language%20Reference.pdf
http://www.ecma-international.org/news/TC45_current_work/TC45_available_docs.htm
https://www.toptal.com/xml/an-informal-introduction-to-docx
<w:t> is for text
<w:r> is for ???
<w:p> is for paragraph


http://officeopenxml.com/WPtextFormatting.php
'''
