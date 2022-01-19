sum = []

t_case = int(input())

for _ in range(t_case):
    n1, n2 = map(int, input().split())

    sum.append(n1+n2)

for i in range(t_case):
    print('Case #'+str(i+1)+": "+str(sum[i]))
