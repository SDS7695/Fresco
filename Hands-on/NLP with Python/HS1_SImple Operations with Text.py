# TASK 1
import nltk
from nltk.book import text6
n = len(text6)
print(n)
u = len(set(text6))
print(u)
wc = n/u
print(wc)

# TASK 2
ise_ending_words = [word for word in set(text6) if word.endswith('ise')]
print(len(ise_ending_words))

# TASK 3
contains_z = [word for word in set(text6) if 'z' in word]
print(len(contains_z))

# TASK 4
contains_pt = [word for word in set(text6) if 'pt' in word]
print(len(contains_pt))

# TASK 5
title_words = [word for word in text6 if (len(word)==1 and word[0].isupper()) or (word[0].isupper() and word[1:].islower()) ]
print(len(title_words))

# TASK 6
text6freq = nltk.FreqDist(text6)
print(text6freq['ARTHUR'])