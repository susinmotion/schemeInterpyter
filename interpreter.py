import math, operator
dictOfVars={}

def tokenize(theString):
	newString=theString.replace("(", " ( ").replace(")"," ) ")
	tokensList=newString.split()
	return tokensList

def listify(theString):
	tokensList=theString
	if type(theString)==str:
		tokensList=tokenize(theString)
	
	throwaway, returnvalue= nestListOnPeren(tokensList)
	return returnvalue[0]

def nestListOnPeren(tokensList):

	index=0
	nestedList=[]
	item=tokensList[0]
	while index<len(tokensList):
		item=tokensList[index]
		index=index+1
		if item == "(":
			newIndex,newChunk=nestListOnPeren(tokensList[index:])
			index=index+newIndex
			nestedList.append(newChunk)

		elif item ==")":
			return index, nestedList

		else:
			nestedList.append(item)
			#index= index+1
	return index, nestedList


def findInnerMost(nestedList):
	returnList=nestedList
	for i in range(len(nestedList)):
		if type(nestedList[i])==list:
			returnList[i]= operate(findInnerMost(nestedList[i]))

	return returnList

def operate(innerMostItem):
	for i in range(len(innerMostItem)):
		innerMostItem[i]=toInt(innerMostItem[i])

	if len(innerMostItem)==1:
		return innerMostItem

	else:
		operator=innerMostItem[0]
		if operator=="define":
			define(innerMostItem[1:])
			return None
		try:
			return domath(operator,innerMostItem[1:])
		except IndexError:
			return operators[operator](innerMostItem[1:])



def toInt(token):
	typeToken=None
	try:
		integer=int(token)
		return integer
	except (ValueError, TypeError):
		if token in dictOfVars.keys():
			return dictOfVars[token]

		elif token in operators.keys():
			return token

		elif token[0]=="'":
			return "quote", token

		else:
			typeToken="unknown"
			return (token)

def evaluate(nestedList):
	#print operate(findInnerMost(tokenize(nestedList)))
	return operate(findInnerMost(listify(nestedList)))

def domath(operator, listOfOperands):

	result=operators[operator](listOfOperands[0],listOfOperands[1])
	if len(listOfOperands)>2:
		restOfList=listOfOperands[2:]
		restOfList.insert(0,result)
		result=domath(operator,restOfList)

	return result

def define(listOfOperands):
	if len(listOfOperands)!=2:

		print "reqires two items"
		print listOfOperands
		quit()
	else:
		if type(listOfOperands[1])==int:
			dictOfVars[listOfOperands[0]]=listOfOperands[1]
		else:
			params=[]
			names=[]
			for items in listOfOperands[0][1:]:
				params.append(items) 
				names.append(str(items))

			operators[listOfOperands[0][0]]=lambda params: makeFun(listOfOperands[1],params, names)
def makeFun(expression, params, names):
	for i in range(len(names)):
		dictOfVars[names[i]]=params[i]

	result= operate (expression)
	return result

def let():
	pass
operators={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.div,"<":operator.lt,">":operator.gt}
math={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.div,"<":operator.lt,">":operator.gt}
creators={"let":let,"define":define,"set!":define,"quote":""}

if __name__ == '__main__':


	while True:
		inputString=raw_input()
		evaluate(inputString)

