# TASK 1
from nltk.corpus import gutenberg
for fileid in gutenberg.fileids():
   n = len(gutenberg.words(fileid))
   u = len(set(gutenberg.words(fileid)))
   print(n/u,  fileid)

# TASK 2
aus_words = gutenberg.words('austen-sense.txt')
aus_words_alpha = [word for word in aus_words if word.isalpha()]
aus_words_gt4_z = [word for word in aus_words_alpha if len(word) > 4 and 'z' in word]
print(len(aus_words_gt4_z))

# TASK 3
aus_unique_words = set([word.lower() for word in aus_words_alpha)])
from nltk.corpus import words
engcorpus_words = words.words()
engcorpus_unique_words = set([word.lower() for word in engcorpus_words])
unusual_words = aus_unique_words.difference(engcorpus_unique_words)
print(len(unusual_words))