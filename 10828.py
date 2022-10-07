import sys

input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
  command = input().split()

  if command[0] == "push":
    stack.append(command[1])
  elif command[0] == "pop":
    value = stack.pop() if stack else -1
    print(value)
  elif command[0] == "top":
    value = stack[len(stack) - 1] if stack else -1
    print(value)
  elif command[0] == "size":
    print(len(stack))
  elif command[0] == "empty":
    print(int(len(stack) == 0))