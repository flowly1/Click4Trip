"""
	This function spilts the input sentence to tokens and filter the unnecessery characters.
	it returns an array of the filtered tokens
"""
def Tokenize(input):
	words=input.split()
	newWords=[]
	for word in words:
		newWords.append(''.join(filter(str.isalpha, word)).lower())
	return RemoveStopWords(newWords)

"""
	This function load the stopwords from a file.
	Those words saved into a set in the global frame.
"""
def LoadStopWords():
	file=open("/home/michaaz/SW.txt","r")
	lines = file.read().splitlines()

	global stopWordsSet
	for line in lines:
		stopWordsSet.add(line)
	file.close()

"""
	This function update the tokens by removing any stopwords that may be among them.
	It returns the new tokens.
"""
def RemoveStopWords(tokens):
	newTokens=[]
	for word in tokens:
		if word not in stopWordsSet:
			newTokens.append(word)
	return newTokens

def getProb(words):
	file=open("/home/michaaz/Training/Dict.txt","r")
	lines=file.read().splitlines()
	# get probability for each of the classification classes (positive and negative)
	sumPos=float(lines.pop(0).split()[1])
	sumNeg=float(lines.pop(0).split()[1])
	# get default probability for unknown word for each classification class (using Laplace Estimation)
	posDef=float(lines.pop(0).split()[2])
	negDef=float(lines.pop(0).split()[2])

	posDic=dict()
	negDic=dict()
	wordsSet=set(words)

	for word in wordsSet:
		count=words.count(word) # count the number of times each word appear in the filtered tokens
		posDic[word]=count
		negDic[word]=count
	posWordsSet=set(wordsSet)
	negWordsSet=set(wordsSet)

	for line in lines: # go over each line only once
		lis=line.split() # split each word in the current line
		if lis[1] in posWordsSet: # if the specific word (from the dictionary) appears in the word set
			if lis[0]=="pos":
				posDic[lis[1]]=float(pow(float(lis[2]),posDic[lis[1]])) # pow(word's existing avarage, number of times this word appears in the input)
				posWordsSet.remove(lis[1])
		if lis[1] in negWordsSet:
			if lis[0]=="neg":
				negDic[lis[1]]=float(pow(float(lis[2]),negDic[lis[1]]))
				negWordsSet.remove(lis[1])
	# words that does not appear in the dictionary (did not learnt)
	for key in posDic:
		if key in posWordsSet:
			posDic[key]=float(pow(posDef,posDic[key]))
		sumPos=sumPos*posDic[key]
	for key in negDic:
		if key in negWordsSet:
			negDic[key]=float(pow(negDef,negDic[key]))
		sumNeg=sumNeg*negDic[key]

	denominator = sumPos+sumNeg
	return [format(100*sumPos/denominator,'.2f')+'%', format(100*sumNeg/denominator,'.2f')+'%']

stopWordsSet=set()
LoadStopWords()
while (1):
	sen=input("Enter Sentance: ")
	prob=getProb(Tokenize(sen))
	print ("Positive: "+ repr(prob[0]))
	print ("Negative: " +repr(prob[1]))
