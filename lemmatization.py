#Lemmatization looks beyond word reduction as shown in stemming.py.
#It looks at surrounding text to determine a given word's part of speech.
#It considers a language's full vocabulary to apply a morphological analysis to words.
#The lemma of 'was' is 'be'.  The lemma of 'mice' is 'mouse'.  The lemma of 'meeting'
#might be 'meet' or 'meeting' depending on its use in a sentence.

import spacy
nlp =spacy.load('en_core_web_sm')

doc1 = nlp(u"I am a runner running in a race because I love to run since I ran today.")

for token in doc1:
    print(token.text, '\t', token.lemma, '\t', token.lemma_)

#Results:
#I        561228191312463089      -PRON-
#am       10382539506755952630    be
#a        11901859001352538922    a
#runner   12640964157389618806    runner
#running          12767647472892411841    run
#in       3002984154512732771     in
#a        11901859001352538922    a
#race     8048469955494714898     race
#because          16950148841647037698    because
#I        561228191312463089      -PRON-
#love     3702023516439754181     love
#to       3791531372978436496     to
#run      12767647472892411841    run
#since    10066841407251338481    since
#I        561228191312463089      -PRON-
#ran      12767647472892411841    run
#today    11042482332948150395    today
#.        12646065887601541794    .