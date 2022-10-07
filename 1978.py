import sys
from math import sqrt
input = sys.stdin.readline

def isPrime(x):
  if x == 1 or x == 0:
    return False

  half_x = x // 2
  for i in range(2, half_x + 1):
    if x % i == 0:
      return False
  return True

n = int(input())
numbers = list(map(int, input().split()))

answer = 0

for x in numbers:
  if isPrime(x):
    answer += 1
    
print(answer)
  