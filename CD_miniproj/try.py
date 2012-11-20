def computeLastUse(d, i, j):
	flag = 1
	k = i-1
	
	if (j>1):
		flag = 0
		k = i+1 #Bcoz k is decremented further
	elif j==0:
		while k>=0 and flag==1:
			if (d[i][j] == d[k][0]):
				flag = 0
			k = k-1
	if flag==1:
		k=0

	return 'lu'+str(k)

def computeNextUse(d, i, j):
	flag = 1
	k = i+1
	while k<len(d) and flag==1:
		l = 2
		while  l<len(d[k]):
			if d[k][l]==d[i][j]:
				flag = 0
			l = l+1
		k = k+1

	if flag == 1:	
		ret = 'nnu'
	else:
		ret = 'nu'+str(k)
	
	return ret

def gen():
	d = []
	f = open ( 'in.txt', 'r')
	lines = f.readlines()
	for i in lines:
		i = i.split('\n')
		d.append(i[0])
	#print d
	i = len(d)-1
	t = []
	k = 0

	while ( i>=0 ):
		j=0
		while (j<len(d[i])):
			if ( d[i][j].isalpha() ):
				temp1 = computeLastUse(d, i, j)
				temp2 = computeNextUse(d, i, j)
				values = [temp1, temp2]
				t.append([d[i][j], values])
				k = k+1
			j = j+1
		i=i-1

	print '\n'
	for i in t:
		print str(i)+'\n'

gen()
