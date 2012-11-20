import usage
import table
import re
import eval
import InfixTopostfix

def call():
	eval.eval()
	d=[]
        f1 = open ( 'inout.txt', 'r')
        lines = f1.readlines()
        for i in lines:
                i = i.split('\n')
                d.append(i[0])

	quad = []
        i = 0
        while(i<len(d)):
                quad.append(re.findall('\w+|\+|-|\*', d[i]))
                i=i+1

	t=[]
	usage.gen(quad, t) # WORKS FINE!!!
	#print output as (var, lux, nuy)
	for i in t:
		print "("+str(i[0])+","+str(i[1][0])+","+str(i[1][1])+")"

	#table.get()

call()
