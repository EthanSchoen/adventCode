import math

text = open('days/day16_input.txt', "r").read()
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 16 ~~~~~~~~~~~~~~~~~~~~~~~~~')

groups = text.split('\n\n')
rules = {}
for r in groups[0].splitlines():
  r = r.split(':')
  i = r[0]
  r = r[1].split(' or ')
  rules[i] = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in r]
mine = [int(i) for i in groups[1].splitlines()[1].split(',')]
nearby = [[int(i) for i in t.split(',')] for t in groups[2].splitlines()[1:]]
invalid = []
for t in nearby:
  for v in t:
    for r in rules.values():
      if r[0][0] <= v <= r[0][1] or r[1][0] <= v <= r[1][1]:
        break
    else:
      invalid.append(v)
print('Part 1:', sum(invalid))

valid = nearby.copy()
for t in nearby:
  for v in t:
    for r in rules.values():
      if r[0][0] <= v <= r[0][1] or r[1][0] <= v <= r[1][1]:
        break
    else:
      valid.remove(t)
      break
col_map = {k : [] for k in rules.keys()}
for r in rules.keys():
  for i in range(len(rules)):
    for t in valid:
      if rules[r][0][0] <= t[i] <= rules[r][0][1] or rules[r][1][0] <= t[i] <= rules[r][1][1]:
        pass
      else:
        break
    else:
      col_map[r].append(i)
multi = 1
taken = set()
loop = True
while loop:
  loop = False
  for r in rules.keys():
    if len(col_map[r]) == 1:
      taken.add(col_map[r][0])
    else:
      new = []
      for i in col_map[r]:
        if not i in taken:
          new.append(i)
      col_map[r] = new
      loop = True
vals = [mine[col_map[k][0]] for k in col_map.keys() if k.split(' ')[0] == 'departure']
print('Part 2:', math.prod(vals))

print()