lines = open('days/day13_input.txt', "r").read().split('\n')
# lines = open('test.txt', "r").read().split('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 13 ~~~~~~~~~~~~~~~~~~~~~~~~~')

bus_id = -1
time = int(lines[0])
earliest = 9999999
for ids in lines[1].split(','):
  if ids == 'x':
    continue
  ids = int(ids)
  next_time = ids *(time//ids) + ids
  if earliest > next_time:
    bus_id = ids
    earliest = next_time
print('Part 1', (earliest-time)*bus_id)

index = 1
ids = [i if i == 'x' else int(i) for i in lines[1].split(',')]
vals = {ids[0]:0}
step = ids[0]
ts = ids[0]
for i in ids[1:]:
  if i == 'x':
    index = index + 1
    continue
  vals[i] = index
  while True:
    if all( (ts+vals[i])%i == 0  for i in vals):
      break
    else:
      ts = ts + step
  step = step * i
  index = index + 1
print('Part 2', ts)

print()