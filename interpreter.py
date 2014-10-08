import math, operator

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
			nestedList.append(typeOfItem(item))
			index= index+1
		item=getNextItem(index,tokensList)

def typeOfItem(token):
	typeToken=None
	try:
		integer=int(token)
		return integer
	except valueError:
		if token in dictOfVars.keys():
			return dictOfVars[token]

		elif token in operators.keys():
			return token
		elif token[0]=="'":
			return "quote", token

		else:
			typeToken="unknown"
			return (token, typeToken)


def findInnerMost(nestedList):
	returnList=[]
	for items in nestedList:
		if type(items)==list:
			returnList.append(operate(findInnerMost(items)))

		else:
			returnList.append(items)
	return returnList


def checkfor_single(scheme_item):
	if len(scheme_item)>1:
		print("invalid syntax")
		quit()
	else:
		item= scheme_item[0]
		return item

def evaluate(nestedList):
	print operate(findInnerMost(tokenize(inputString)))


def domath(operator, listOfOperands):
	result=operators[operator](listOfOperands[0],listOfOperands[1])
	if len(listOfOperands)>2:
		restOfList=listOfOperands[2:]
		restOfList.insert(0,result)
		result=domath(operator,restOfList)

	return result

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
		if operator in operators.keys():
			result=domath(operator,items)

	return result


def add(listOfOperands):
	result=0
	for items in listOfOperands:
		result=result+int(items)
	return result

def subtract(listOfOperands):
	result=int(listOfOperands[0])
	for items in listOfOperands[1:]:
		result=result-int(items)
	return result

def multiply(listOfOperands):
	result=1
	for items in listOfOperands:
		result=result*int(items)
	return result

def divide(listOfOperands):
	numerator=float(listOfOperands[0])
	for items in listOfOperands[1:]:
		print numerator
		numerator=numerator/float(items)

	return numerator

def less(listOfOperands):
	firstNum=listOfOperands[0]
	for nums in listOfOperands[1:]:
		if nums > firstNum:
			return False
	return True


def define(listOfOperands):
	if len(listOfOperands)!=2:
		print "reqires two items"
		quit()
	else:
		dictOfVars[listOfOperands[0]]=listOfOperands[1]

operators={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.div,"<":operator.lt,">":operator.gt,"define":"","quote":""}

if __name__ == '__main__':

	dictOfVars={}
	while True:
		inputString=raw_input()
		evaluate(inputString)

