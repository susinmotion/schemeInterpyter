def tokenize(theString):
	newString=theString.replace("(", " ( ").replace(")"," ) ")
	tokensList=newString.split()
	if tokensList[0] !="(":
		nestedList=checkfor_single(tokensList)
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

"""def findInnerMost(nestedList):
	returnList=[]
	index=0
	for items in nestedList:
		index=index+1
		print "items", items, "index", index
		if type(items)==list:
			findInnerMost(list)
			result= operate (items)
			nestedList[index-1] =result
			returnList.append(result)
			findInnerMost(nestedList)

		else:
			returnList.append(items)
	print returnList
	return operate(returnList)"""

def findInnerMost(nestedList):
	returnList=[]
	for items in nestedList:
		if type(items)==list:
			returnList.append(operate(findInnerMost(items)))

		else:
			returnList.append(items)
	print returnList
	return returnList


def checkfor_single(scheme_item):
	if len(scheme_item)>1:
		print("invalid syntax")
		quit()
	else:
		item= scheme_item[0]
		return item

def evaluate(nestedList):
	scheme_item=findInnerMost(nestedList)
	while scheme_item:
		nestedList[index]=operate(scheme_item)
		scheme_item, index=findInnerMost(nestedList)


def operate(scheme_item):
	result=None
	if len(scheme_item)==1:
		return scheme_item
	else:
		operator=scheme_item[0]
	index=0
	for items in scheme_item[1:]:
		index=index+1
		if type(items)==list:
			scheme_item[index]==findInnerMost(scheme_item)
	if operator== "+":
		result=add(scheme_item[1:])
	elif operator== "-":
		result=subtract(scheme_item[1:])
	elif operator=="*":
		result=multiply(scheme_item[1:])

	return result


def add(listOfOperands):
	result=0
	for items in listOfOperands:
		result=result+int(items)
	return result

def subtract(listOfOperands):
	result=0
	for items in listOfOperands:
		result=result-int(items)
	return result

def multiply(listOfOperands):
	result=1
	for items in listOfOperands:
		result=result*int(items)
	return result

def divide(listOfOperands):
	numerator=listOfOperands[0]
	for items in listOfOperands[1:]:
		numerator=numerator/items

	return numerator
