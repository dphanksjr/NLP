import spacy

nlp = spacy.load('en_core_web_sm')
from spacy.matcher import Matcher

###Token matching for rule based matching example###

matcher = Matcher(nlp.vocab)

pattern1 = [{'LOWER':'solarpower'}]
pattern2 = [{'LOWER':'solar'},{'IS_PUNCT':True},{'LOWER':'power'}]
pattern3 = [{'LOWER':'solar'},{'LOWER':'power'}]

matcher.add('SolarPower', None, pattern1,pattern2,pattern3)

doc = nlp(u"The Solar Power industry continues to grow a solarpower increases.  Solar-Power is amazing.")
found_matches=matcher(doc)

print(found_matches)
#Results:
#8656102463236116519 SolarPower 1 3 Solar Power
#8656102463236116519 SolarPower 8 9 solarpower
#8656102463236116519 SolarPower 12 15 Solar-Power

for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(match_id, string_id, start, end, span.text)

#####phrase matcher#####

from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

with open('reaganomics.txt', encoding='cp1252') as f:
    doc3=nlp(f.read())

phrase_list=['voodoo economics', 'supply-side economics', 'trickle-down economics','free-market economics']

phrase_patterns = [nlp(text) for text in phrase_list]

type(phrase_patters[0])

matcher.add('EconMatcher', None, *phrase_patterns)

found_matches = matcher(doc3)

print(found_matches)
#Results:
#[(3680293220734633682, 41, 45), (3680293220734633682, 49, 53), (3680293220734633682, 54, 56), 
# (3680293220734633682, 61, 65), (3680293220734633682, 673, 677), (3680293220734633682, 2985, 2989)]

for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc3[start-5:end+5] #adds 5 characters before and 5 characters after found match
    print(match_id, string_id, start, end, span.text)

#Results of for loop:
#3680293220734633682 EconMatcher 41 45 policies are commonly associated with supply-side economics, referred to as trickle
#3680293220734633682 EconMatcher 49 53 economics, referred to as trickle-down economics or voodoo economics by political
#3680293220734633682 EconMatcher 54 56 trickle-down economics or voodoo economics by political opponents, and
#3680293220734633682 EconMatcher 61 65 by political opponents, and free-market economics by political advocates.
#3680293220734633682 EconMatcher 673 677 attracted a following from the supply-side economics movement, which formed in
#3680293220734633682 EconMatcher 2985 2989 became widely known as "trickle-down economics", due to the

