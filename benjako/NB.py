def Tokenize(input):
	words=input.split()
	newWords=[]
	for word in words:
		newWords.append(''.join(filter(str.isalpha, word)).lower())
	return newWords

def getProb(words):
	file=open("/home/benjako/Training/Dict.txt","r")
	lines=file.read().splitlines()
	sumPos=float(lines.pop(0).split()[1])
	sumNeg=float(lines.pop(0).split()[1])
	posDef=float(lines.pop(0).split()[2])
	negDef=float(lines.pop(0).split()[2])
	posDic=dict()
	negDic=dict()
	wordsSet=set(words)
	for word in wordsSet:
		count=words.count(word)
		posDic[word]=count
		negDic[word]=count
	posWordsSet=set(wordsSet)
	negWordsSet=set(wordsSet)
	for line in lines:
		lis=line.split()
		if lis[1] in posWordsSet:
			if lis[0]=="pos":
				posDic[lis[1]]=float(pow(float(lis[2]),posDic[lis[1]]))
				posWordsSet.remove(lis[1])
		elif lis[1] in negWordsSet:
			if  lis[0]=="neg":
				negDic[lis[1]]=float(pow(float(lis[2]),negDic[lis[1]]))
				negWordsSet.remove(lis[1])
	for key in posDic:
		if key in posWordsSet:
			posDic[key]=float(pow(posDef,posDic[key]))
		sumPos=sumPos*posDic[key]
	for key in negDic:
		if key in negWordsSet:
			negDic[key]=float(pow(negDef,negDic[key]))
		sumNeg=sumNeg*negDic[key]
	return [sumPos, sumNeg]

while (1):
	sen=input("Enter Sentance: ")
	prob=getProb(Tokenize(sen))
	print ("Positive: "+ repr(prob[0]))
	print ("Negative: " +repr(prob[1]))
