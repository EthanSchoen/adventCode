import time
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 15 ~~~~~~~~~~~~~~~~~~~~~~~~~')

numbers = [0,3,6]
record, new = {n: i for i, n in enumerate(numbers[:len(numbers)-1])}, numbers[len(numbers)-1]
for turn in range(4, 2021):
  last = new
  new = 0 if not last in record else turn - 2 - record[last]
  record[last] = turn - 2
print('Part 1:', new)

t = time.time()
numbers = [12,1,16,3,11,0]
record, new = {n: i for i, n in enumerate(numbers[:len(numbers)-1])}, numbers[len(numbers)-1]
for turn in range(7, 30000001):
  last = new
  new = 0 if not last in record else turn - 2 - record[last]
  record[last] = turn - 2
print('Part 2:', new)

print()