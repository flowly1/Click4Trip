"""
	This function get a file, open it and return two parameters:
		1. An array of all the lines
		2. Total lenght of lines
"""
def GetLinesAndNum(fileName):
	file=open(fileName,"r")
	lines=file.read().splitlines()
	file.close()
	return [lines,len(lines)]

"""
	This function get all the lines and creates two data sets:
		1. An array of all the words.
		2. A set of all the words (without repeats).
"""
def GetWordsAndSet(sentences):
	words=[]
	wordsSet=set()
	for sen in sentences:
		senWords=sen.split()
		for word in senWords:
			words.append(word)
			wordsSet.add(word)
	return [words, wordsSet]

"""
	This function creates a dictionary. The key is the word, the value is the number of times this word appears.
"""
def GetDict(wordSet,words):
	Dict=dict()
	for word in wordSet:
		Dict[word]=0
	for word in  words:
		Dict[word]=Dict[word]+1
	return Dict

"""
	This function creates a dictionary with all the words and the number of thier appearences.
	It returns the dictionary and the number of lines it has.
"""
def GetDictAndSenNum(file):
	lines, senNum=GetLinesAndNum(file)
	words, wordsSet=GetWordsAndSet(lines)
	Dict=GetDict(wordsSet,words)
	return [Dict, senNum]

"""
	This function calculates the probability for each word using the Laplace Estimation model.
	It returns:
		1. the dictionary containing the words and thier probability.
		2. total number of lines.
		3. total number of words.
"""
def GetProbDict(file):
	Dict, senNum=GetDictAndSenNum(file)
	wordSize=0
	dictVals=Dict.values()
	for wordCount in dictVals: # get number of total words
		wordSize=wordSize+wordCount+1
	ProbDict=dict()
	for key in Dict:
		ProbDict[key]=((Dict[key]+1)/wordSize) # set the probability for each word in the dictionary according to the Naive Bayes algorithm
	return [ProbDict, senNum, wordSize]

def WriteToFile():
	print ("Dict Probability writing started")
	posProbDict, posSenNum, posWordsSize=GetProbDict("pos.txt")
	print ("POS Probability Done")
	negProbDict, negSenNum, negWordsSize=GetProbDict("neg.txt")
	print ("NEG Probability Done")
	file=open("Dict.txt","w")
	# calculate probability for positive and negative sentence
	posProb=posSenNum/(posSenNum+negSenNum)
	negProb=negSenNum/(posSenNum+negSenNum)

	file.write("PosProb "+repr(posProb)+"\n")
	file.write("NegProb "+repr(negProb)+"\n")
	# probability for an unknown word in each of the classification classes
	file.write("POS * "+repr((1/posWordsSize))+"\n")
	file.write("NEG * "+repr((1/negWordsSize))+"\n")
	# write each of the probability dictionaries in a text file
	for key in posProbDict:
		file.write("pos "+key+" "+repr(posProbDict[key])+"\n")
	for key in negProbDict:
		file.write("neg "+key+" "+repr(negProbDict[key])+"\n")
	file.close()

WriteToFile()
print("Done :D")
