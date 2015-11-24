import os, nltk, re, random
from math import sqrt

stopwords = nltk.corpus.stopwords.words('english')
K = 3
ITERATIONS = 15

# Returns a dictionary {<filename>:[array of tokens]}
def readDocs(docPath):
	docTokens = {}
	# Switch to doc directory using path
	previous_dir = os.getcwd()
	os.chdir(docPath)
	for file in os.listdir('.'):
		if file.endswith('.txt'):
			# Reads all text documents in a directory
			fOpen = open(file, 'r', encoding='utf-8', errors='ignore')
			fRead = fOpen.read()
			docTokens[file] = [w.lower() for w in nltk.word_tokenize(fRead) if w.lower() not in stopwords and re.compile(r'^[a-z]+$').search(w.lower())]
	return docTokens

# Returns the vocab of a set of documents
def getVocab(docTokens):
	vocab = set()
	for key in docTokens:
		vocab = vocab.union(docTokens[key])
	return vocab

# Returns the vector representation of a document for a given vocabulary
def getDocVector(doc, vocab, vectorIndex):
	vector = [0] * len(vectorIndex)
	for word in docTokens[doc]:
		vector[vectorIndex[word]] += 1
	return vector

# Returns K seeds from the list of vectors
def selectRandomSeeds(vectors, K):
	# Get K random document names
	docSeeds = random.sample(list(vectors), K)
	# Get the vectors for each random document name
	seeds = [vectors[d] for d in docSeeds]
	return seeds

# Euclidean distance between vectors
def dist(x, c):
	sqdist = 0.
	for i in range(len(x)):
		sqdist += (x[i] - c[i]) ** 2
	return sqrt(sqdist)

# returns the mean vector of a list of vectors
def vectorMean(vectors):
	c = [0]*len(vectors[0])
	for vector in vectors:
		for i in range(len(vector)):
			c[i] += vector[i]
	for i in range(len(c)):
		c[i] /= len(vectors)
	return c

def kmeans(docVectors, K):
	seeds = selectRandomSeeds(docVectors, K)

	for i in range(0, ITERATIONS):
		w = [None]*K
		for k in range(K):
			w[k] = []

		dists = [None]*K
		for d in docVectors:
			dists = [dist(seeds[s], docVectors[d]) for s in range(len(seeds))]
			j = dists.index(min(dists))
			w[j].append(docVectors[d])

		for k in range(K):
			seeds[k] = vectorMean(w[k])
		return seeds


# Get document tokens
docTokens = readDocs('.')
# Get vocab of the set of documents
vocab = getVocab(docTokens)

# Initialize vector index
vectorIndex = {}
offset = 0
for word in vocab:
	vectorIndex[word] = offset
	offset += 1
# Get vectors for each document
docVectors = {}
for doc in docTokens:
	docVectors[doc] = getDocVector(doc, vocab, vectorIndex)

clusters = kmeans(docVectors, K)
for c in clusters:
	print(c)















