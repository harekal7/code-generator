def push_stack(stackArr,ele):
    stackArr.append(ele)

def pop_stack(stackArr):
    return stackArr.pop()

def isOperand(who):
    if(not(isOperator(who)) and (who != "(") and (who != ")")):
        return 1
    return 0

def isOperator(who):
    if(who == "+" or who == "-" or who == "*" or who == "/" ):
        return 1
    return 0

def topStack(stackArr):
    return(stackArr[len(stackArr)-1])

def isEmpty(stackArr):
    if(len(stackArr) == 0):
        return 1
    return 0

def prcd(who):
    if(who == "^"):
	return(5)
    if((who == "*") or (who == "/")):
	return(4)
    if((who == "+") or (who == "-")):
	return(3)
    if(who == "("):
	return(2)
    if(who == ")"):
	return(1)

def InfixToPostfix(infixStr,postfixStr = []):
    postfixStr = []
    stackArr = []
    postfixPtr = 0
    tempStr = infixStr
    infixStr = []
    infixStr = strToTokens(tempStr)
    for x in infixStr:
	if(isOperand(x)):
            postfixStr.append(x+' ')
        if(isOperator(x)):
        	while((not(isEmpty(stackArr))) and (prcd(x) <= prcd(topStack(stackArr)))):
                    postfixStr.append(topStack(stackArr))
                    pop_stack(stackArr)
       		push_stack(stackArr,x)

        elif(x == "("):
                push_stack(stackArr,x)                
        elif(x == ")"):
            while(topStack(stackArr) != "("):
                postfixStr.append(pop_stack(stackArr))
            pop_stack(stackArr)
            
    while(not(isEmpty(stackArr))):
        if(topStack(stackArr) == "("):
            pop_stack(stackArr)#may be raise exception
        else:
            postfixStr.append(pop_stack(stackArr))

    return(postfixStr)


def strToTokens(infix):
    strArr = []
    strArr = infix
    tempStr = ''	
    tokens = []
    tokens_index = 0
    count = 0
    for x in strArr:
        count = count+1
        if(isOperand(x)):
            tempStr += x
        if(isOperator(x) or x == ")" or x == "("):
            if(tempStr != ""):
                tokens.append(tempStr)
                tokens_index = tokens_index+1
            tempStr = ''
            tokens.append(x)
            tokens_index = tokens_index+1 
        if(count == len(strArr)):
            if(tempStr != ''):
                tokens.append(tempStr)
    return(tokens)



def conversion(infixExpr):
        postfixExpr=InfixToPostfix(infixExpr)
	print postfixExpr
	
	l=[]
    	for x in postfixExpr:
        	if(isOperand(x)):
        		l.append(x)
    	f = open("symbol_original.txt", "w")
    	for i in l:
       		newline = i.rstrip('\r\n')
        	f.write(newline)
        	f.write('\n')
	f.close()
	return postfixExpr			
          
        

#menu()
