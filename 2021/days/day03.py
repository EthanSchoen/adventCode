
input = open('days/day03_input.txt', "r").read().split('\n')
size = len(input[0])

print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 3 ~~~~~~~~~~~~~~~~~~~~~~~~~')

def get_counts(inp):
  counts = [[0, 0] for _ in range(size)]
  for l in inp:
    for i in range(size):
      if l[i] == '1':
        counts[i][1] += 1
      else:
        counts[i][0] += 1
  return counts

# Part 1
def part1():
  counts = get_counts(input)
  gamma = int(''.join(list(map(lambda x: '1' if x[1] > x[0] else '0', counts))), 2)
  epsilon = int(''.join(list(map(lambda x: '1' if x[1] < x[0] else '0', counts))), 2)
  return gamma * epsilon

# Part 2
def part2():
  o2, co2 = input.copy(), input.copy()
  pos = 0
  while len(o2) > 1 and pos < size:
    c = get_counts(o2)
    if (c[pos][1] >= c[pos][0]):
      o2 = list(filter(lambda x: x[pos] == '1', o2))
    else:
      o2 = list(filter(lambda x: x[pos] == '0', o2))
    pos += 1
  pos = 0
  while len(co2) > 1 and pos < size:
    c = get_counts(co2)
    if (c[pos][1] < c[pos][0]):
      co2 = list(filter(lambda x: x[pos] == '1', co2))
    else:
      co2 = list(filter(lambda x: x[pos] == '0', co2))
    pos += 1
  return int(o2[0], 2) * int(co2[0], 2)

print('part1: ' + str(part1()))
print('part2: ' + str(part2()))
print()
