import math, operator
dictOfVars={}

def tokenize(theString):
	newString=theString.replace("(", " ( ").replace(")"," ) ")
	tokensList=newString.split()
	return tokensList
	"""if tokensList[0] !="(":
		nestedList=checkfor_single(tokensList)
	else:
		throwaway, nestedList= nestListOnPeren(tokensList)
	return nestedList"""

def output(theString):
	tokensList=theString
	if type(theString)==str:
		tokensList=tokenize(theString)
	
	throwaway, returnvalue= nestListOnPeren(tokensList)
	return returnvalue[0]
#def getNextItem(index, theList):
#	if index>len(theList):
#		return None
#
#	return theList[index]

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
			nestedList.append(typeOfItem(item))
			#index= index+1
	return index, nestedList

def typeOfItem(token):
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


def findInnerMost(nestedList):
	returnList=[]
	if nestedList[0]=="define":
		define(nestedList[1:])
		return None
	for items in nestedList:
		if type(items)==list:
			returnList.append(operate(findInnerMost(items)))

		else:
			returnList.append(items)
	return returnList



"""def checkfor_single(scheme_item):
	if len(scheme_item)>1:
		print("invalid syntax")
		quit()
	else:
		item= scheme_item[0]
		return item"""

def evaluate(nestedList):
	#print operate(findInnerMost(tokenize(nestedList)))
	return operate(findInnerMost(output(nestedList)))

def domath(operator, listOfOperands):
	for items in listOfOperands:
		if type(items) != int:
			return None
	else:
		result=operators[operator](listOfOperands[0],listOfOperands[1])
		if len(listOfOperands)>2:
			restOfList=listOfOperands[2:]
			restOfList.insert(0,result)
			result=domath(operator,restOfList)

		return result

def operate(scheme_item):
	result=scheme_item
	if len(scheme_item)==1:
		return result
	else:
		operator=scheme_item[0]
	index=0
	for items in scheme_item[1:]:
		index=index+1
		if type(items)==list:
			scheme_item[index]==findInnerMost(scheme_item)
	if operator in operators.keys():
		try:
			result=domath(operator,scheme_item[1:])
		except IndexError:
			result=operators[operator](scheme_item[1:])

#this is getting done too many times when we run this function on a homemade function

	"""if operator in creators.keys():
		creators[operator](scheme_item[1:])
		return None"""


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
	"""if len(names)==1:
					dictOfVars[names[0]]=params[0]
				else:"""
	for i in range(len(names)):
		dictOfVars[names[i]]=params[i]

	for i in range(len(expression)):
		expression[i] = typeOfItem(expression[i])
	print expression
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

