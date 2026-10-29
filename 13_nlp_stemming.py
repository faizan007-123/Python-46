#============================================================================

import nltk 

from nltk.stem import LancasterStemmer


ls = LancasterStemmer()



print(ls.stem('playing'))
print(ls.stem('running'))

#============================================================================

import nltk

from nltk.stem import PorterStemmer

ws=PorterStemmer()

print(ws.stem('eating'))
print(ws.stem('running'))

#============================================================================

from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("english")

words = ["playing", "played", "plays", "running", "runs"]

for word in words:
    print(word, ":", stemmer.stem(word))
