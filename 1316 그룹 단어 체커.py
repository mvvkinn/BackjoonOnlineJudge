def mergeLappedAlpha(word):
	word = list(word)
	listlen = len(word)

	size = 0
	i=0
	
	while size < listlen: #사ㄱ제도ㅣㄴ 무ㄴ자에 따라 기ㄹ이 유도ㅇ저ㄱ으로 조저ㄹ
		while i < size:
			if word[i] == word[i+1]:
				del word[i]
				listlen=len(word)
				
				size = 0
				i = 0
				continue
			i+=1
		size+=1
	return word
	
def isGroup(word, mergedword):
	wordset = list(set(word))
	
	setlen = len(wordset)
	mergedlen = len(mergedword)
	
	i=0
	j=0
	
	while i<setlen:
		while j<mergedlen:
			if wordset[i] == mergedword[j]:
				del wordset[i]
				del mergedword[j]
				
				setlen = len(wordset)
				mergedlen = len(mergedword)
				
				#print(wordset)
				#print(mergedword)
				
				if setlen == 0:
					break
					
				
				
				i=0
				j=0
				
				continue
			j+=1
		i+=1
	if len(mergedword)>0:
		print(False)
		return False
	elif len(mergedword) == 0:
		print(True)
		return True

testcase = int(input())

cnt = 0

for i in range(testcase):
	word = input()
	word = word.upper()
	
	merged = mergeLappedAlpha(word)
	if isGroup(word, merged) == True:
		cnt+=1
		
print(cnt)
