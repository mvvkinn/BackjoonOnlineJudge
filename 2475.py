from functools import reduce

sample = "0 4 2 5 6"
numbers = list(
  map(lambda x: x ** 2, 
      list(map(int, sample.split())))
)

print(sum(numbers) % 10)

