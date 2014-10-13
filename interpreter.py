import math, operator
dictOfVars={'y':5}

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


def findInnerMost(nestedList, currentVars=dictOfVars):
	returnList=nestedList
	for i in range(len(nestedList)):
		if type(nestedList[i])==list:
			returnList[i]= operate(findInnerMost(nestedList[i]), currentVars)

	return returnList

def operate(innerMostItem, currentVars=dictOfVars):
	operator=innerMostItem[0]
	if len(innerMostItem)==1:
		return innerMostItem[0]

	elif operator in operators.keys():
			
		if operator=="define":
			define(innerMostItem[1:])
			return None
		elif operator=="let":
			return let(innerMostItem[1:])

		return domath(operator,innerMostItem[1:], currentVars)

	else:
		return innerMostItem

def toInt(token, currentVars=dictOfVars):
	typeToken=None
	try:
		integer=int(token)
		return integer
	except (ValueError, TypeError):
		if token in currentVars.keys():
			return int(currentVars[token])

		elif token in operators.keys():
			return token

		elif token[0]=="'":
			return "quote", token

		else:
			typeToken="unknown"
			return (token)

def evaluate(nestedList):
	#print operate(findInnerMost(tokenize(nestedList)))
	tokenized=listify(nestedList)
	if tokenized[0] in creators.keys():
		return creators[tokenized[0]](tokenized[1:])
	return operate(findInnerMost(listify(nestedList)))

def domath(operator, listOfOperands, currentVars=dictOfVars):
	for i in range(len(listOfOperands)):
		listOfOperands[i]=toInt(listOfOperands[i], currentVars)
		if type(listOfOperands[i]) != int:
			listOfOperands.insert(0, operator)
			return listOfOperands
	if len(listOfOperands)==1:
		return operators[operator](listOfOperands)
	else:
		result=operators[operator](listOfOperands[0],listOfOperands[1])

	if len(listOfOperands)>2:
		restOfList=listOfOperands[2:]
		restOfList.insert(0,result)
		result=domath(operator,restOfList, currentVars)
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



def let(listOfOperands, currentVars=dictOfVars):
	for items in listOfOperands[0]:
		currentVars[items[0]]=items[1]
	result=operate(findInnerMost(listOfOperands[1:],currentVars))
	return result
	

def makeFun(expression, params, names):
	currentVars=dictOfVars
	for i in range(len(names)):
		currentVars[names[i]]=params[i]

	result= operate(findInnerMost(expression, currentVars))
	return result

operators={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.div,"<":operator.lt,">":operator.gt, "let":let}
math={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.div,"<":operator.lt,">":operator.gt }
creators={"let":let,"define":define,"set!":define,"quote":""}

if __name__ == '__main__':


	while True:
		inputString=raw_input()
		evaluate(inputString)

