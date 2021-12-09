
input = open('days/day01_input.txt', "r").read().split('\n')
numbers = list(map(int, input))

print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 1 ~~~~~~~~~~~~~~~~~~~~~~~~~')

# Part 1
def part1():
  count = 0
  last = numbers[0]
  for n in numbers[1:]:
    if n > last:
      count += 1
    last = n
  return count

# Part 2
def part2():
  window = numbers[:4]
  count = 1 if sum(window[0:3]) < sum(window[1:4]) else 0
  for n in numbers[4:]:
    window = window[1:]
    window.append(n)
    if sum(window[0:3]) < sum(window[1:4]):
      count += 1
  return count

print('part1: ' + str(part1()))
print('part2: ' + str(part2()))
print()
