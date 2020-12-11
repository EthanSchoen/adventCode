import math

lines = open('days/day10_input.txt', "r").read().split('\n')
lines = open('test.txt', "r").read().split('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 10 ~~~~~~~~~~~~~~~~~~~~~~~~~')

def count_diffs(adapters):
  last = 0
  res = {'one': 0, 'two': 0, 'three': 0}
  for a in adapters:
    if a - last == 1:
      res['one'] = res['one'] + 1
    if a - last == 2:
      res['two'] = res['two'] + 1
    if a - last == 3:
      res['three'] = res['three'] + 1
    last = a
  return res
def num_arangements(adapters):
  if len(adapters) == 2:
    return 1
  if len(adapters) == 3:
    return 2
  return 2**(len(adapters)-1)

adapters = [int(l) for l in lines]
adapters.sort()
adapters.append(adapters[len(adapters)-1]+3)
res = count_diffs(adapters)
print('Part 1:', res['one']*res['three'])

adapters.reverse()
batch = []
last = adapters[0]
configs = 1
for a in adapters[1:]:
  if last-a == 3:
    if len(batch) > 1:
      configs = configs * num_arangements(batch)
    batch = [a]
  else:
    batch.insert(0, a)
  last = a
print('Part 2:', configs)

print()