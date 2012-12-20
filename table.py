import sys

def is_nnu_present(reg , inst_no , t):
	
	present = False
	
	for i in reg:
		if(t[inst_no][reg.index(i)][1] == None):
			present = True
			break

	return present

def nnu_register(reg ,inst_no, t):
	
	index = -1
	for i in reg:
		if(t[inst_no][i][1] == None):
			index = reg.index(i)
			break
	return index

def is_address_descriptor(table , reg):
		
	present = False		
	for i in reg:
		
		if(table[i][0] != None and table[i][1] != None):
			table[i][1] = None
			present = True
			break
	return present


def address_descriptor(table , reg):
	
	for i in reg:
	
		free = -1	
		if(table[i][0] != None and table[i][1] != None):
			table[i][1] = None
			free = reg.index(i)
			break
	return free 



def get_operation(quad):
	
	if(quad[2] == '+'):
		return 'ADD'
	elif(quad[2] == '-'):
		return 'SUB'
	elif(quad[3] == '*'):
		return 'MUL'





def next_use_register(reg , inst_no , t):
	
	a = []
	for i in reg:
		a.append(t[inst_no][i][1])

	
	b = a
	
	b.sort()
	index = a.index(b[-1])
	return index
	
			
def getReg_and_update1(I , inst_no , reg , table , t):

	print 
	print 
	print I
	print 
	print 	
		
	if I[1] in reg:
		first_op = reg.index(I[1])
		
	elif None in reg:
	
		free = reg.index(None)
		reg[free] = I[1]

	
		table[I[1]][1] = free
		print '*'*40	
		print 'LOAD R' , free , ' , ' ,I[1]
		first_op = free
	else:
		
		if(is_address_descriptor(table , reg)):
		
			
			free = address_descriptor(table , reg)
			if(free != -1):
				reg[free] = I[1]
				table[I[1]][1] = free
				print 'LOAD R',free , ' , ' , I[1]
				first_op = free
			
		
		elif(I[0] in reg):
			free = reg.index(I[0])
			reg[free] = I[1]
			
			table[I[0]][1] = None
			table[I[1]][1] = free
		
			print 'LOAD R' , free , ' , ' , I[1]
			
			first_op = free
		

		elif(is_nnu_present(reg , inst_no ,  t)):
			free = nnu_register(reg ,inst_no, t)
			
			reg[free] = I[1]
			table[I[1]][1] = free
		
			print ('LOAD R' , free , ' , ' , I[1])
			first_op = free
	
		else:
			free = next_use_register(reg , inst_no , t)
                        print 'STORE ' , reg[free] , ' R ' , free
                        table[reg[free]][1] = None
                        reg[free] = I[1]
                        table[I[1]][1] = free
                        first_op = free

		
	if I[3] in reg:
		
		second_op = reg.index(I[3])
	elif None in reg:
	
		free = reg.index(None)
		reg[free] = I[1]

	
		table[I[3]][1] = free
		print '*'*40	
		print 'LOAD R' , free , ' , ' ,I[3]
		
		second_op = free
	else:
		
		if(is_address_descriptor(table , reg)):

                        free = address_descriptor(table , reg)
			if(free != -1):
                        	reg[free] = I[3]
                        	table[I[3]][1] = free
                        	print 'LOAD R',free , ' , ' , I[3]
				second_op = free
		
		elif(I[0] in reg):
			free = reg.index(I[0])
			reg[free] = I[1]
			
			table[I[0]][1] = None
			table[I[1]][1] = free
		
			print 'LOAD R' , free , ' , ' , I[3]

			second_op = free
		

		elif(is_nnu_present(reg , inst_no ,  t)):
			free = nnu_register(reg ,inst_no, t)
			
			reg[free] = I[3]
			table[I[3]][1] = free
		
			print 'LOAD R' , free , ' , ' , I[3]
			second_op = free
		else:
			free = next_use_register(reg , inst_no , t)
			print 'STORE ' , reg[free] , ' R ' , free
			table[reg[free]][1] = None
			reg[free] = I[3]
			table[I[3]][1] = free
			second_op = free
				

	
	if(I[0] == I[1]):

		free = table[I[1]][1]
		table[I[1]][1] = None
		reg[free] = I[0]
		table[I[0]][1] = free

		print get_operation(quad) ,' R ',free ,' R ', free , ' R ' , second_op
		
	elif(I[0] == I[3]):
		free = table[I[3]][1]
		table[I[3]][1] = None
		reg[free] = I[0]
		table[I[0]][1] = free

		print get_operation(quad) , ' R ' , first_op , ' R ' , free , ' R ' , free

	
		
		
			

def get(quad , t):

	try:
		r = int(raw_input('enter the no of registers , minimum - 3\n'))
		if r < 3:
			raise
	except:
		#prigennt ' \nInvalid Input.... Exiting..'
		print '\nInvalid Input.... Exiting..'		
		sys.exit()

	reg = []
	for i in range(0 , r):
		reg.append(None)


	f_original = open('symbol_original.txt' , 'r')
	f_temp = open('symbol_temp.txt' , 'r')

	lines_original = f_original.readlines()
	lines_temp     = f_temp.readlines()

	original_variables = []
	for i in lines_original:
		i = i.split('\n')
		original_variables.append(i[0])


	temp_variables = []
	for i in lines_temp:
		i = i.split('\n')
		temp_variables.append(i[0])

	table = dict({})

	for i in original_variables:
		table[i] = [i , None]


	
	for i in temp_variables:
		table[i] = [None , None]

	print
	print	
	print reg
	print
	print table
'''
	k = 0
	for i in quad:

		if(len(quad[k]) > 2):
			getReg_and_update1(i , quad.index(i) , reg , table , t)
			
		else:
			pass
			#getReg_and_update2(i , quad.index(i) , reg , table ,t)
		k = k + 1
'''
