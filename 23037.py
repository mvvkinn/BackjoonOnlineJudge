import math

input_str = input()

sum = 0

for num in input_str:
    po = pow(int(num), 5)
    sum = sum + po

print(sum)
