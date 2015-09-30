#
# Thomas Plonski
#

import nltk, os

query = input("Enter words by order of importance: ")

query = query.split()
print (query)

dict = {query[0] : 0.6, query[1]: 0.4 }

string = ""

print (dict)
for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        fOpen = open(file, "r")
        fRead = fOpen.read()
        for i in fRead:
            string += i

token = nltk.word_tokenize(string)
#print (token)

worth = 0

for q, v in dict.items():
    for t in token:
        if (q == t):
            worth = worth + v
            break
print (worth)

