
input = open('days/day05_input.txt', "r").read().split('\n')
lines = []
for l in input:
  parts = l.split(' ')
  lines.append(dict(start=[int(i) for i in parts[0].split(',')], end=[int(i) for i in parts[2].split(',')]))

size = 1000
start1 = [[0 for _ in range(size)] for _ in range(size)]
start2 = [[0 for _ in range(size)] for _ in range(size)]

print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 5 ~~~~~~~~~~~~~~~~~~~~~~~~~')

# Part 1
def part1(chart):
  for l in lines:
    if l['start'][0] == l['end'][0] or l['start'][1] == l['end'][1]:
      x_range = [l['start'][0], l['end'][0]]
      y_range = [l['start'][1], l['end'][1]]
      x_range.sort()
      y_range.sort()
      for x in range(x_range[0], x_range[1]+1):
        for y in range(y_range[0], y_range[1]+1):
          chart[x][y] += 1
  count = 0
  for r in chart:
    for x in r:
      if x > 1:
        count += 1
  return count

# Part 2
def part2(chart):
  for l in lines:
    x_range = [l['start'][0], l['end'][0]]
    y_range = [l['start'][1], l['end'][1]]
    if l['start'][0] == l['end'][0] or l['start'][1] == l['end'][1]:
      x_range.sort()
      y_range.sort()
      for x in range(x_range[0], x_range[1]+1):
        for y in range(y_range[0], y_range[1]+1):
          chart[x][y] += 1
    else:
      x_slope = 1 if x_range[0] < x_range[1] else -1
      y_slope = 1 if y_range[0] < y_range[1] else -1
      for s in range(abs(x_range[0]- x_range[1])+1):
        chart[l['start'][0] + (x_slope * s)][l['start'][1] + (y_slope * s)] += 1
  count = 0
  for r in chart:
    for x in r:
      if x > 1:
        count += 1
  return count

print('part1: ' + str(part1(start1)))
print('part2: ' + str(part2(start2)))
print()
