#Stemming is a method for cataloging related words; 
# it chops off letters from the end until the stem is reached.

import nltk

#Example of Porter's Algorith - stemming tool developed by Martin Porter in 1980
#This algorithm employs 5 phases of word reduction, each with its own set of mapping rules
#ponies -> poni; ties -> ti; cats -> cat
from nltk.stem.porter import PorterStemmer

p_stemmer = PorterStemmer()

words = ['run', 'runner', 'ran', 'runs', 'easily', 'fairly']

for word in words:
    print(word + '----->' + p_stemmer.stem(word))

#Results: run----->run
#runner----->runner
#ran----->ran
#runs----->run
#easily----->easili
#fairly----->fairli
#############################################
#Snowball was also developed by Martin Porter
#It offers a slight improvement over the original Porter stemmer in both logic and speed

from nltk.stem.snowball import SnowballStemmer

s_stemmer = SnowballStemmer(language='english')

for word in words:
    print(word + '----->' + s_stemmer.stem(word))

#Results:
#run----->run
#runner----->runner
#ran----->ran
#runs----->run
#easily----->easili
#fairly----->fair

words = ['generous', 'generation', 'generously', 'generate']

for word in words:
    print(word + '----->' + s_stemmer.stem(word))
#Results:
#generous----->generous
#generation----->generat
#generously----->generous
#generate----->generat