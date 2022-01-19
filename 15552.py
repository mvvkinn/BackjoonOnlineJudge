import sys

test_c = int(sys.stdin.readline().rstrip())

for _ in range(test_c):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)