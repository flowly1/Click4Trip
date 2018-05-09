def GetLinesAndNum(fileName):
	file=open(fileName,"r")
	lines=file.read().splitlines()
	file.close()
	return [lines,len(lines)]

def GetWordsAndSet(sentences):
	words=[]
	wordsSet=set()
	for sen in sentences:
		senWords=sen.split()
		for word in senWords:
			words.append(word)
			wordsSet.add(word)
	return [words, wordsSet]

def GetDict(wordSet,words):
	Dict=dict()
	for word in wordSet:
		Dict[word]=0
	for word in  words:
		Dict[word]=Dict[word]+1
	return Dict

def GetDictAndSenNum(file):
	lines, senNum=GetLinesAndNum(file)
	words, wordsSet=GetWordsAndSet(lines)
	Dict=GetDict(wordsSet,words)
	return [Dict, senNum]

def GetProbDict(file):
	Dict, senNum=GetDictAndSenNum(file)
	wordSize=0
	dictVals=Dict.values()
	for wordCount in dictVals:
		wordSize=wordSize+wordCount+1
	ProbDict=dict()
	for key in Dict:
		ProbDict[key]=((Dict[key]+1)/wordSize)
	return [ProbDict, senNum, wordSize]

def WriteToFile():
	print ("Dict Probability writing started")
	posProbDict, posSenNum, posWordsSize=GetProbDict("pos.txt")
	print ("POS Probability Done")
	negProbDict, negSenNum, negWordsSize=GetProbDict("neg.txt")
	print ("NEG Probability Done")
	file=open("Dict.txt","w")
	posProb=posSenNum/(posSenNum+negSenNum)
	negProb=negSenNum/(posSenNum+negSenNum)
	file.write("PosProb "+repr(posProb)+"\n")
	file.write("NegProb "+repr(negProb)+"\n")
	file.write("POS * "+repr((1/posWordsSize))+"\n")
	file.write("NEG * "+repr((1/negWordsSize))+"\n")
	for key in posProbDict:
		file.write("pos "+key+" "+repr(posProbDict[key])+"\n")
	for key in negProbDict:
		file.write("neg "+key+" "+repr(negProbDict[key])+"\n")
	file.close()

WriteToFile()
print("Done :D")
