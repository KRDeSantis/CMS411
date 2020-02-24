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

#document = zipfile.Zipfile("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx")

zipfile.ZipFile("Copy of Sources Sought Synopsis Manuals 8 Jan 2020.docx", 'r')



