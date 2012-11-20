import InfixTopostfix
import re

def eval():
	exp = InfixTopostfix.menu()
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


	quad = re.findall('\w+|\+|-|\*|/|=', exp)
	quad.reverse()
	#print quad

	i = 0
	m=0
	for j in quad:
		#if(VarCount==2):
		#	t=str(varstack.pop())+str(opstack.pop())+str(varstack.pop())
		#	temp.append(t)
		#	varstack.append(temp[k])
		#	k=k+1
		#	VarCount=1	
		if(InfixTopostfix.isOperator(j)):
			#print "OPERATOR INSIDE"
			opstack.append(j)
	
		elif ( VarCount !=2 and InfixTopostfix.isOperand(j)):
			#print "INSIDE"
			varstack.append(j)
			VarCount=VarCount+1
	
		if ( VarCount == 2 ):
			#print varstack
			t=str(varstack.pop())+str(opstack.pop())+str(varstack.pop())
			temp.append(t)
			varstack.append("t"+str(k))
			#varstack.pop()
	       	        k=k+1
			VarCount=1
	i = 0
	t = []
	for l in temp:
		if ( i<count-1 ):
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
