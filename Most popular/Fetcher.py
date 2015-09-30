####
####                    20 most popular words on a website
####                        By Thomas Plonski
####


import nltk, bs4, urllib
from urllib import request
from bs4 import BeautifulSoup
import re
from nltk import text

import string

# Getting the text from the html and converting it into tokens
website = "http://academics.smcvt.edu/vtgeographic/textbook/weather/weather_and_climate_of_vermont.htm"
page = request.urlopen(website)
nohtml = BeautifulSoup(page).get_text()
tokens = nltk.word_tokenize(nohtml)

# Converting the tokens into a single string
totalString = " ".join(tokens)

# Gets rid of the punctuation
regex = re.compile('[%s]' % re.escape(string.punctuation))
totalString = (regex.sub('', totalString))

# Gets the websites contents in tokens
tokened = nltk.tokenize.word_tokenize(totalString)

total = ""
# Converts the website to tokens
for w in tokened:
    total = total + " " + w
print (total)
# Counts the frequency of word usage token by token
counted = nltk.text.Counter(tokened)

# Writes the text of the website onto a text file
webFile = open("websiteText.txt", "w")
webFile.write(total)
# Prints the 20 most counted words
print (counted.most_common(20))

keys = []
# Takes the words out of the tuple that contains the 20 most popular words and makes it into a list
for words in counted.most_common(20):
    keys.append(words[0])

# Converts the list "keys" into a single string to allow for writing to text file
k = " ".join(keys)

# Writes the string that contains the 20 most popular words into a txt file
file = open("output1.txt", "w")
file.write(k)


print (keys)        # Text of the website
print (k)           # 20 most common words (no count)