#Named-entity recognition(NER) locates and classifes named entity mentions in unstructured text into
#pre-defined categories such as the person names, organizations, locations, etc.

import spacy
nlp=spacy.load('en_core_web_sm')

def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + ' - '+ent.label_ + ' - ' +str(spacy.explain(ent.label_)))
        else:
            print('No entities found')

doc = nlp(u'Hi how are you?')

show_ents(doc)

doc=nlp(u"May I go to Washington, DC next May to see the Washington Monument?")
show_ents(doc)

#RESULT: Washington, DC - GPE - Countries, cities, states
#next May - DATE - Absolute or relative dates or periods
#the Washington Monument - ORG - Companies, agencies, institutions, etc.