#최대한 적은수의 봉지
#5킬로, 3킬로

n = int(input())

result = 0

while n != 0:
  if n < 3:
    result = -1
    break
    
  if n % 5 == 0:
    result += n // 5
    break

  result += 1
  n -= 3

  

print(result)