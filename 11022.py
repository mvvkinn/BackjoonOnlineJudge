sum = []

t_case = int(input())

for _ in range(t_case):
    n1, n2 = map(int, input().split())

    formula_str = str(n1) + " + " + str(n2) + " = " + str(n1+n2)

    sum.append(formula_str)

for i in range(t_case):
    print('Case #'+str(i+1)+": ", end='')
    print(sum[i])
