def getDigit(num):
	pow_index = 0
	
	while True:
		temp = num//(10**pow_index)
		if temp>0:
			pow_index=pow_index+1
		else:
			pow_index=pow_index-1
			break
	return pow_index
	

num = int(input())

cnt = num%100 #100이하느ㄴ 드ㅇ차수여ㄹ

digit = getDigit(num)

if digit>=2:
	for i in range(num):
		
