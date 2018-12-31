#Spacy is an open source nlp library released in 2015.
#It's designed to handle NLP tasks with the most efficient implementation of common algorithms
#You don't have the option to choose other algorthims as it has already chosen the most efficient 
#algorithm that is currently avaiable.  It's much faster and more efficient than NLTK.
#It does not include pre-created models for sentiment analysis however.

import spacy

nlp=spacy.load('en_core_web_sm')

mystring='"We\'re moving to L.A.!"'
print(mystring)

doc = nlp(mystring)

for token in doc:
    print(token.text)

from spacy import displacy

doc = nlp(u"Apple is going to build a U.K factory for $6 million.")
displacy.serve(doc,style='dep')