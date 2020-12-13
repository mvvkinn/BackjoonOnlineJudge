#def getEachNum(num): #자리수 하ㅁ수
#	numlist=[]
#	divided=num
#	
#	mod = 1
#		
#	while mod!=0:	
#		if mod == 0:
#			break
#		mod = divided%10
#		divided = divided//10
#		numlist.append(mod)
#	numlist.reverse()
#	return numlist

def getEachNum(str):	
	numbers = []
	for i in range(len(str)):
		numbers.append(str[i])
	return numbers

cons = [1, 2, 3, 5, 6, 7, 9, 15]

c = []

for i in range(15):
	if i not in cons:
		print(i)
		c.append(i+i)
print(c)
