def inputOX(): #받아서 X있는곳 없애서 O배열 만들기
    OX_input = input()
    OX = OX_input.split('X')
    return ' '.join(OX).split()

def getResult(arr): #결과값 구하기
    factorial = 0
    for i in range(len(arr)):
        #factorial = 0
        for j in range(len(arr[i])+1):
            factorial = factorial+j
            #print(factorial)
    return factorial

testcase = int(input())

sum = []

for i in range(testcase):
    quiz = inputOX()
    sum.append(getResult(quiz))
    
for i in range(len(sum)):
    print(sum[i])
