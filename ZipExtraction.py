# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 12:07:55 2020

@author: Thomas Csorba

Turn a docx file into a stream of XML information
"""

import zipfile
import xml.dom.minidom
import docx2txt
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

document = zipfile.ZipFile("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx")

#zipfile.ZipFile("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx", 'r')
docString = document.read("word/document.xml")
docXArr = []
dik = str(docString)
docXArr = dik.split("<w")
#print(docString)

for sent in docXArr:
    print(sent)

#print(document.read("word/document.xml"))
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
