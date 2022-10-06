sample = "8 6 7 1 2 4 3 5"

cords = list(map(int, sample.split()))

result = ""

for i in range(len(cords) - 1):
  diff = cords[i + 1] - cords[i]
  if abs(diff) != 1:
    result = "mixed"
    break
    
  if diff > 0:
    result = "ascending"
  elif diff < 0:
    result = "descending"
    
print(result)
