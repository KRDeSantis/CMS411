#   This file was attempting to see if spacy was installed properly, and to test some of
#   its functionality.
#
import spacy

def main():
    #Load the library we want
    nlp = spacy.load("en_core_web_sm")
    #Load the document/sentences in
    doc = nlp("Apple is looking at closing stores in China due to the outbreak")
    #print the text, lemma (root of the word), part of speech, detailed part of speech tag, syntactic dependency, shape of the word, like capitalization and length,
    #is the token an alpha character, and is the word part of a stop list
    for token in doc:
        print(token.text, " ", token.lemma_, " ", token.pos_, " ", token.tag_, " ", token.dep_, " ", token.shape_, " ", token.is_alpha, " ", token.is_alpha, " ", token.is_stop)
      
main()
