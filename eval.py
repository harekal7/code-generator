import InfixTopostfix
import re

def eval():
	exp = InfixTopostfix.menu()
	print exp
	count=0
	for i in exp:
		#print(i)
		if(InfixTopostfix.isOperator(i)):
      	 	 	count=count+1
	#print "No of temp reqd "+str(count-1)
	temp = [] # temporary variable -> contains 
	VarCount=0 # to count the variables, whether it is ready to be operated on (i.e, 2 vars )
	opstack=[] # stack for operator
	varstack=[] # stack for operand
	k=0
	t=""


	post = re.findall('\w+|\+|-|\*|/|=', exp)
	#post.reverse()
	#print quad
	#a b c * +
	#a, stack <- a
	#b, stack <- b
	#c, stack <- c
	#*, pop -> x, pop -> y, stack <- y * x
	#+, pop -> x, pop -> y, stack <- y + x
	#stack is empty, so pop as result

	k=0
	for i in post:
		if InfixTopostfix.isOperator(i):
			x = varstack.pop()
			y = varstack.pop()
			t=y+i+x
			#varstack.append(y+i+x)
			#print y+i+x
			temp.append(t)
			varstack.append("t"+str(k))
			k=k+1
			
		else:
			varstack.append(i)



#sudo pkill sankarshan -9
#	i = 0
#	m=0
#	for j in quad:
#		flag = InfixTopostfix.isOperand(j)
#		#if(VarCount==2):
#		#	t=str(varstack.pop())+str(opstack.pop())+str(varstack.pop())
#		#	temp.append(t)
#		#	varstack.append(temp[k])
#		#	k=k+1
#		#	VarCount=1	
#		if(InfixTopostfix.isOperator(j)):
#			#print "OPERATOR INSIDE"
#			opstack.append(j)
#	
#		elif ( VarCount !=2 and InfixTopostfix.isOperand(j)):
#			#print "INSIDE"
#			varstack.append(j)
#			VarCount=VarCount+1
#	
#		if ( VarCount == 2 ):
#			#print varstack
#			var1 = varstack.pop()
#			var2 = varstack.pop()
#			t=str(var1)+str(opstack.pop())+str(var2)
#			temp.append(t)
#			varstack.append("t"+str(k))
#			#varstack.pop()
#	       	        k=k+1
#			VarCount=1

	i = 0
	t = []
	for l in temp:
		if i<count-1:
			t.append("t"+str(i)+"="+str(l))
		else:
			t.append(str(l))
		i=i+1
	
	f = open("inout.txt", "w")
	print '\n'
	for i in t:
		print i
		f.write(i)
		f.write('\n')
	print '\n'
