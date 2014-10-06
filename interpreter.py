def tokenize(theString):
	newString=theString.replace("(", " ( ").replace(")"," ) ")
	tokensList=newString.split()
	if tokensList[0] !="(":
		if len(tokensList)>1:
			print("invalid syntax")
			quit()
		else:
			nestedList= tokensList[0]
	else:
		throwaway, nestedList= nestListOnPeren(tokensList)

	return nestedList

def getNextItem(index, theList):
	if index>len(theList):
		return None

	return theList[index]

def nestListOnPeren(tokensList):

	index=1
	nestedList=[]
	item=getNextItem(index,tokensList)
	while item:
		if item == "(":
			newIndex,newChunk=nestListOnPeren(tokensList[index:])
			index=index+newIndex
			nestedList.append(newChunk)

		elif item ==")":
			return index+1, nestedList

		else:
			nestedList.append(item)
			index= index+1
		item=getNextItem(index,tokensList)

def evaluate(newList):
	print "new list coming in is", newList
	return "hi!"