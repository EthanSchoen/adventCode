print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 15 ~~~~~~~~~~~~~~~~~~~~~~~~~')

numbers = [int(i) for i in [0,3,6]]
turn = len(numbers) + 1
new = 0
while True:
  last = numbers[len(numbers) - 1]
  try:
    new = numbers[::-1].index(last, numbers[::-1].index(last)+1) - numbers[::-1].index(last)
  except:
    new = 0
  numbers.append(new)
  if turn == 2020:
    break
  turn = turn + 1
print('Part 1:', new)

numbers = [int(i) for i in [12,1,16,3,11,0]]
turn = len(numbers) + 1
new = 0
record = {}
for i, n in enumerate(numbers[:len(numbers)-1]):
  record[n] = i
while True:
  last = numbers[len(numbers) - 1]
  if not last in record:
    new = 0
  else:
    new = turn - 2 - record[last]
  numbers.append(new)
  record[last] = turn - 2
  if turn == 30000000:
    break
  turn = turn + 1
print('Part 2:', new)

print()