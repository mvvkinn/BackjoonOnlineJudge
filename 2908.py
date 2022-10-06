numbers = list(map(
  lambda x: int("".join(reversed(x))), input().split()
))

print(max(numbers))