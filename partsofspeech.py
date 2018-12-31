import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")

print(doc.text)

print(doc[4].pos_)
#Result: VERB

for token in doc:
    print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")

#RESULT:
#The        DET        DT         determiner
#quick      ADJ        JJ         adjective
#brown      ADJ        JJ         adjective
#fox        NOUN       NN         noun, singular or mass
#jumped     VERB       VBD        verb, past tense
#over       ADP        IN         conjunction, subordinating or preposition
#the        DET        DT         determiner
#lazy       ADJ        JJ         adjective
#dog        NOUN       NN         noun, singular or mass
#'s         PART       POS        possessive ending
#back       NOUN       NN         noun, singular or mass
#.          PUNCT      .          punctuation mark, sentence closer

###The example below shows how spacy can note the difference in present and past tense based
###on the context of the sentence.

doc = nlp(u"I read books on NLP.")

word = doc[1]

word.text

token = word
print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")
#RESULT: read       VERB       VBP        verb, non-3rd person singular present

doc=nlp(u"I read a book on NLP.")
word = doc[1]

token = word
print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")
#RESULT: read       VERB       VBD        verb, past tense