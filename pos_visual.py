import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")

from spacy import displacy

displacy.serve(doc, style="dep", options={'distance':110})