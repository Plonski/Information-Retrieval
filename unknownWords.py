__author__ = 'Thomas Plonski'

#
#   Prints words that are not defined in nlkt.corpus.words.words, that aren't stopwords
#   Prints a list of the most common bigrams (letters that are next adjacent to each other)
#   Prints the most common words in the html, does not include stopwords
#   Prints the most common word thats not a stopword and its frequency
#

from bs4 import BeautifulSoup
from urllib import request
import nltk
from nltk.collocations import *
from nltk.corpus import words, stopwords
import re


url = input("Website is :")                         #   Asks for a url and adds http:// to the url if it does not contain so already
try:
    e = request.urlopen(url)                        #   Opens the URL and retrieves the html
except:
    url = "http://" + url
    e = request.urlopen(url)

p = BeautifulSoup(e).get_text()                 #   Retrieves the text from the html
tokenedWords = nltk.word_tokenize(p)                       #   Tokenizes the text

textString = ""
textString = " ".join(tokenedWords)

unW = []

def unknown(list):

    k = re.findall(r'(?<= )+[a-z]+\b', textString)       # Removes punctuation and capitalized words
    print(textString)
    for w in k:                                          # Gets all the words
        if(w not in words.words()):                      # If  website words arent in NLTK word dictionary:
            unW.append(w)                                # Adds the word to the unknown list
    print (unW)                                          # Prints words that are not in the NLTK word dictionary

unknown(tokenedWords)

'''
The most interesting part about the unknown word list that I got when I searched a website was that they were real words
but they contained stems that prevented them from being recognized as known.
Some examples of words that should have been picked up but weren't due to a stem:

largest, friends, skills, recognised

This exhibits the need for the removal of stems to get the base of the words in order to get an accurate idea of which
words are truely unusual.
'''

def bigrams(list):
    allWords = re.findall(r'\w',textString)                     # Gets all words
    conjoined = "".join(allWords)                               # Joins the words together into a single string that is conjoined
    conOutput = nltk.bigrams(conjoined)
    fdist = nltk.FreqDist(conOutput)
    print (fdist.most_common(10))                               # Prints 10 most common bigrams

bigrams(tokenedWords)


def characteristicWord(list):
    stop = stopwords.words("english")
    candidateWords = []
    k = re.findall(r'(?<= )+[a-z]+\b', textString)       # Removes punctuation and capitalized words
    for w in k:                                          # Gets all the words
        if(w not in stopwords.words("english")):         # If  website words are in NLTK stopword dictionary:
            candidateWords.append(w)                     # Adds the word to the unknown list

    print (candidateWords)                               # Prints words that are not in the NLTK stopword dictionary
    characterword = nltk.FreqDist(candidateWords)
    print(characterword.most_common(1))                  # Most common word that isnt a stopword
characteristicWord(tokenedWords)