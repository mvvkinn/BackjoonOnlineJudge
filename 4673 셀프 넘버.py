def getEachNum(str):	
	numbers = []
	for i in range(len(str)):
		numbers.append(int(str[i]))
	return numbers
	
cons = []
	
for i in range(1, 10000):
	if i not in cons:
		dn = i
		while True:
			eachnum = getEachNum(str(dn))
			dn = sum(eachnum)+dn
			if dn>=10000 or dn in cons:
				break
			cons.append(dn)

for i in range(1, 10000):
	if i not in cons:
		print(i)
		
