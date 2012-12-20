import InfixTopostfix
#import postfix
import re

def eval(expression, k):
	exp = InfixTopostfix.menu(expression)
	#exp = postfix.menu(expression)
	#print exp
	count=0
	for i in exp:
		#print(i)
		if(InfixTopostfix.isOperator(i)):
      	 	#if(postfix.isOperator(i)):
		 	count=count+1
	temp = [] # temporary variable -> contains 
	VarCount=0 # to count the variables, whether it is ready to be operated on (i.e, 2 vars )
	opstack=[] # stack for operator
	varstack=[] # stack for operand
	t=""
	exp = str(exp)
	post = re.findall('\w+|\+|-|\*|/|=', exp)
	#print post
        l=[]
        for x in post:
                if(InfixTopostfix.isOperand(x)):
                        l.append(x)

        f = open("symbol_original.txt", "w")
        for i in l:
                newline = i
                f.write(newline)
                f.write('\n')
        f.close()

	store_i = k
	temp_list=[]
	temps = ''
	for i in post:
		if InfixTopostfix.isOperator(i):
		#if postfix.isOperator(i):
			x = varstack.pop()
			y = varstack.pop()
			t=y+i+x
			temp.append(t)
			if ( i!='=' ):
				temps = "t"+str(k)
				#print i+"harekal"+temps
				temp_list.append(temps)
				varstack.append(temps)
				k=k+1
			
		else:
			varstack.append(i)

	f = open("symbol_temp.txt", "w")
	for i in temp_list:
     		f.write(i)
        	f.write('\n')
    	f.close()

	i = store_i
	t = []
	for l in temp:
		if i<store_i+count-1:
			#print l
			t.append("t"+str(i)+"="+str(l))
		else:
			t.append(str(l))
		i=i+1
	

	f = open("inout.txt", "a")
	for i in t:
		print i
		f.write(i)
		f.write('\n')
	f.close()
	return k
