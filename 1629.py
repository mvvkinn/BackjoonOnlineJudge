import math

m1, m2, d1 = map(int, input().split())

result = m1

# 지수 반으로 나눠 계산
result = math.pow(m1, int(m2/2))

# 지수 짝수면 *2 후 나눔
if m2%2 == 0:
    result = int(result*2 % d1)

# 지수 홀수면 *m1 후 나눔
else:
    result = int(result* m1 % d1)

print(result)
