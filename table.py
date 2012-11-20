import sys

def init_table(des, regs, var):
        update = []
	update.append([])
	update.append([])
        for i in regs:
                update[0].append(None)

        for i in var:
                if ( var[i] =='act' ):
                        update[1].append(i)
                else:
                        update[1].append(None)

        des.append(update)

def display_table(des):
        #i = 0
	print des[0],des[1]
	i = 2
        while (i<len(des)):
                print des[i],
                i = i+1
		print

def update(des):
	update = []
	update.append(['a', 'b', None])
	update.append(['a', 'c', 'b', 'd,R1', None, None, 'R0'])
	#des.append(update[0])
	des.append(update)

def get():
	try:
		r = int(raw_input("Enter the numeber of registers (minimum 3)"))
		if r<3:
			raise
	except:
		print '\nInvalid Input.. Exiting\n'
		sys.exit()
	
	print '\n'
	regs = []
	i=0
	while (i<r):
		regs.append ( "R"+str(i) )
       		i = i + 1


	#getActualVars()
	#getTempVars()
	#as of now, this is hardcoded
	var = {}
	var['a']='act'
	var['b']='act'
	var['c']='act'
	var['d']='act'
	var['t']='temp'
	var['u']='temp'
	var['v']='temp'

	var_list = []
	for i in var:
		var_list.append(i)

	#Register and Address Descripters
	des = [regs, var_list]
	
	init_table(des, regs, var)
	#display_table(des)
	update(des)
	print '\n\n'
	print des
	print '\n\n'
	display_table(des)
