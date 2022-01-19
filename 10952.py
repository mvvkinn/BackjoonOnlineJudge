sum = []

while(True):
    n1, n2 = map(int, input().split())
    
    if n1 == 0 and n2 == 0:
      break
    else:
        sum.append(n1+n2)

for i in range(len(sum)):
    print(sum[i])
