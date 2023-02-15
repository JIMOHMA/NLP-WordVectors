# All Import Statements Defined Here
# Note: Do not add to this list.
# All the dependencies you need, can be installed by running .
# ----------------

import sys
assert sys.version_info[0]==3
assert sys.version_info[1] >= 5

from gensim.models import KeyedVectors
from gensim.test.utils import datapath
import pprint
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [10, 5]
import nltk
nltk.download('reuters')
from nltk.corpus import reuters
import numpy as np
import random
import scipy as sp
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import PCA

START_TOKEN = '<START>'
END_TOKEN = '<END>'

np.random.seed(0)
random.seed(0)
# ----------------


def read_corpus(category="crude"):
    """ Read files from the specified Reuter's category.
        Params:
            category (string): category name
        Return:
            list of lists, with words from each of the processed files
    """
    files = reuters.fileids(category)
    return [[START_TOKEN] + [w.lower() for w in list(reuters.words(f))] + [END_TOKEN] for f in files]

#### DISPLAYING TO SEE WHAT THE INFORMATION IN THE CORPUS LOOKS LIKE
# reuters_corpus = read_corpus()
# pprint.pprint(reuters_corpus[:3], compact=True, width=100)

# check for real word except for ' in a word
# ' can only occur once
# length of word > 1
# other symbols not present in the work e.g , ? / > < \ ] 
def validAppostrophy(word):
    if (word.find("'") != -1):
        tempword = word.replace("'", '')
        if (len(word) > 1 and word.count("'") == 1 and tempword.isalpha()):
            return True
    return False

def distinct_words(corpus):
    """ Determine a list of distinct words for the corpus.
        Params:
            corpus (list of list of strings): corpus of documents
        Return:
            corpus_words (list of strings): list of distinct words across the corpus, sorted (using python 'sorted' function)
            num_corpus_words (integer): number of distinct words across the corpus
    """
    corpus_words = []
    num_corpus_words = -1
    
    # remove words that have numbers in them
    # remove symbols e.g @, ?, /, ., -, =
    # HINT: Regex may help here
    corpus = [['START'] + [realWord for realWord in list if realWord.isalpha() or validAppostrophy(realWord)] + ['END'] for list in corpus]
    
#     tempCorpus = []
#     for wordList in corpus:
#         corpus = wordList + tempCorpus
        
#     corpus = list(corpus)
        
    temp_words = set()
    for sentence in corpus:
        for word in sentence:
            temp_words.add(word)
    corpus_words = sorted(list(temp_words))
    num_corpus_words = len(corpus_words)
    
    return corpus_words, num_corpus_words


    # ---------------------
# Run this sanity check
# Note that this not an exhaustive check for correctness.
# ---------------------

# Define toy corpus
test_corpus = ["START All that glitters isn't gold ' END".split(" "), "START All's well that ends well END".split(" ")]
test_corpus_words, num_corpus_words = distinct_words(test_corpus)
print(test_corpus_words, num_corpus_words)

# Correct answers
ans_test_corpus_words = sorted(list(set(["START", "All", "ends", "that", "gold", "All's", "glitters", "isn't", "well", "END"])))
ans_num_corpus_words = len(ans_test_corpus_words)

# Test correct number of words
assert(num_corpus_words == ans_num_corpus_words), "Incorrect number of distinct words. Correct: {}. Yours: {}".format(ans_num_corpus_words, num_corpus_words)

# Test correct words
assert (test_corpus_words == ans_test_corpus_words), "Incorrect corpus_words.\nCorrect: {}\nYours:   {}".format(str(ans_test_corpus_words), str(test_corpus_words))

# Print Success
print ("-" * 80)
print("Passed All Tests!")
print ("-" * 80)