import re

def computeLastUse(quad, i, j):
	flag = 1
	k = i-1
	
	if (j>0):
		flag = 0
		k = i+1 #Bcoz k is decremented further
	elif j==0:
		while k>=0 and flag==1:
			if (quad[i][j] == quad[k][0]):
				flag = 0
			k = k-1
	if flag==1:
		k=0

	return 'lu'+str(k)

def computeNextUse(quad, i, j):
	flag = 1
	k = i+1
	while k<len(quad) and flag==1:
		l = 1
		while  l<len(quad[k]):
			if quad[k][l]==quad[i][j]:
				flag = 0
			l = l+1
		k = k+1

	if flag == 1:	
		ret = 'nnu'
	else:
		ret = 'nu'+str(k)
	
	return ret

def gen(quad, t):
	i=len(quad)-1

	while(i>=0):
		j = 0
		while (j<len(quad[i])):
			if ( j!=2 ):
				#print quad[i][j]
				lu = computeLastUse(quad, i, j)
				nu = computeNextUse(quad, i, j)
				t.append([quad[i][j], [lu, nu]])
			j = j+1
		i = i-1
	
