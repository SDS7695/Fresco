# TASK 1
import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist([(genre, word.lower()) for genre in brown.categories() for word in brown.words(categories=genre) ])
print(cfd.tabulate(conditions=['news','religion','romance'], samples=['can', 'could', 'may', 'might', 'must', 'will']))

# TASK 2
from nltk.corpus import inaugural
ac_cfd = nltk.ConditionalFreqDist([(fileid[:4],word.lower()[:7]) for fileid in inaugural.fileids() for word in inaugural.words(fileid)])
print(ac_cfd.tabulate(conditions =['1841', '1993'],  samples=['america', 'citizen'] ))