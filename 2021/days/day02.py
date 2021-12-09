
input = open('days/day02_input.txt', "r").read().split('\n')

print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 2 ~~~~~~~~~~~~~~~~~~~~~~~~~')

# Part 1
def part1():
  x, y = 0, 0
  for line in input:
    d, v = line.split(' ')
    v = int(v)
    if d == 'up':
      y -= v
    elif d == 'down':
      y += v
    elif d == 'forward':
      x += v
  return x * y

# Part 2
def part2():
  a, x, y = 0, 0, 0
  for line in input:
    d, v = line.split(' ')
    v = int(v)
    if d == 'up':
      a -= v
    elif d == 'down':
      a += v
    elif d == 'forward':
      x += v
      y += a * v
  return x * y

print('part1: ' + str(part1()))
print('part2: ' + str(part2()))
print()
