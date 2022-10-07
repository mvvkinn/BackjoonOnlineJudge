import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
queue = deque()

for _ in range(n):
  command = input().split()

  if command[0] == "push":
    queue.append(command[1])
  elif command[0] == "pop":
    value = queue.popleft() if queue else -1
    print(value)
  elif command[0] == "back":
    value = queue[len(queue) - 1] if queue else -1
    print(value)
  elif command[0] == "front":
    value = queue[0] if queue else -1
    print(value)
  elif command[0] == "size":
    print(len(queue))
  elif command[0] == "empty":
    print(int(len(queue) == 0))