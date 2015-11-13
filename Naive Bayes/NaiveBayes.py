# -*- coding: utf-8 -*-

import os
import nltk
import math
#nltk stopwords - english
stopwords = nltk.corpus.stopwords.words('english')
#nltk regular expression tokenizer
RT = nltk.RegexpTokenizer(r'\w+')
#Initializing tokens, documents, text lists
tokens = []
D = []
text = []
#Initializing counter for each class
animalsDocCount = 0
birdsDocCount = 0
treesDocCount = 0
#getting training set documents dynamically and separate them into different classes
for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        if file.startswith("D"):
            fOpen = open(file, "r+")
            fRead = fOpen.read()
            terms = RT.tokenize(fRead)
            terms = [w.lower() for w in terms if w.lower() not in stopwords]
            if file[1:-4] == "1" or file[1:-4]=="2" or file[1:-4]=="3" or file[1:-4]=="4":
                D.append([int(file[1:-4]),file[:-4],"animals",terms])
                animalsDocCount = animalsDocCount + 1
            elif file[1:-4]=="5" or file[1:-4]=="6" or file[1:-4]=="7":
                D.append([int(file[1:-4]),file[:-4],"birds",terms])
                birdsDocCount = birdsDocCount + 1
            else:
                D.append([int(file[1:-4]),file[:-4],"trees",terms])
                treesDocCount = treesDocCount + 1
            tokens.append(terms)
#Total Number of documents
N = len(D)
#finding dictionary of training set
for t in tokens:
   text = text + t
V = set(text)
print("\nTraining set vocabulary: ", V)
#Calculating probability of each class
priorC = [["animals", animalsDocCount/N],["birds", birdsDocCount], ["trees", treesDocCount]]
print("\nProbability (priorC) of each class in the training set: ", priorC)
#initializing textC(includes each class's tokens)
textC = []
textAnimalClass = []
textBirdClass = []
textTreeClass = []
#finding each class tokens
for doc in D:
    if "animals" in doc:
        textAnimalClass = textAnimalClass + doc.pop()
    elif "birds" in doc:
        textBirdClass = textBirdClass + doc.pop()
    else:
        textTreeClass = textTreeClass + doc.pop()
textC.append(["animals", textAnimalClass])
textC.append(["birds", textBirdClass])
textC.append(["trees", textTreeClass])
#Intializing each class's Tct and TctCount
animalsTct = []
birdsTct = []
treesTct = []
animalTctCount = 0
birdTctCount = 0
treeTctCount = 0
#calculating each class's Tct list and TctCount
for textc in textC:
    if "animals" in textc:
        for t in V:
            animalsTct.append([t, textc[1].count(t), 0])
            animalTctCount = animalTctCount + textC[1].count(t) + 1
    elif "birds" in textc:
        for t in V:
            birdsTct.append([t, textc[1].count(t), 0])
            birdTctCount = birdTctCount + textC[1].count(t) + 1
    else:
        for t in V:
            treesTct.append([t, textc[1].count(t), 0])
            treeTctCount = treeTctCount + textC[1].count(t) + 1
#calculating conditional probability of each term belongs to its class(for each class)
print("\nConditional Probability of each term in animals class: ")
for t in animalsTct:
    t[2] = (t[1] + 1)/animalTctCount
    print([t[0],t[2]])
print("\nConditional Probability of each term in birds class: ")
for t in birdsTct:
    t[2] = (t[1] + 1)/birdTctCount
    print([t[0],t[2]])
print("\nConditional Probability of each term in trees class: ")
for t in treesTct:
    t[2] = (t[1] + 1)/treeTctCount
    print([t[0],t[2]])
#reading test document
testDoc = open("testDoc1.txt","r")
testTokens = testDoc.read()
testTokens = RT.tokenize(testTokens)
#eleminating stopwords from tokens of test document
testTokens = set([w.lower() for w in testTokens if w.lower() not in stopwords])
for t in V:
    W = [val for val in testTokens if val in V]
print("\nterms of test documents that are in tarining set vocabulary: ", W)
#initializing scores(for each class)
scores = []
animalScore = 0
birdScore = 0
treeScore = 0
#calculating log value of each class's priorC
for each in priorC:
    if "animals" in each:
        animalScore = math.log(each[1])
    elif "animals" in each:
        birdScore = math.log(each[1])
    else:
        treeScore = math.log(each[1])
#calculating scores of each class for the given test document
for t in W:
    for tct in animalsTct:
        if t in tct:
            animalScore = animalScore + math.log(tct[2])
    for tct in birdsTct:
        if t in tct:
            birdScore = birdScore + math.log(tct[2])
    for tct in treesTct:
        if t in tct:
            treeScore = treeScore + math.log(tct[2])
scores.append(["animals", animalScore])
scores.append(["birds", birdScore])
scores.append(["trees", treeScore])
print("\nThe scores of each class for the test document are: ", scores)
#sorting final list to get the maximum score
scores = sorted(scores,  key=lambda tup: tup[1])
print("\nThe given test document belogns to: ", scores.pop())
