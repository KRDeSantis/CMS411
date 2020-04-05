import spacy

def main():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Apple is looking at closing stores in China due to the outbreak")

    for token in doc:
        print(token.text, " ", token.lemma_, " ", token.pos_, " ", token.tag_, " ", token.dep_, " ", token.shape_, " ", token.is_alpha, " ", token.is_alpha, " ", token.is_stop)
      
main()
