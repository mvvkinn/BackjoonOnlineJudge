t = int(input())

arr_n = []
arr_str = []

for _ in range(t):
  input_n, input_str = input().split()
  arr_n.append(int(input_n))
  arr_str.append(input_str)

for i in range(t):
  for str in arr_str[i]:
    for n in range(arr_n[i]):
      print(str, end="")
  print("")
