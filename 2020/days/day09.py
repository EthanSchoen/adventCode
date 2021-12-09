lines = open('days/day09_input.txt', "r").read().split('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 9 ~~~~~~~~~~~~~~~~~~~~~~~~~')

def is_sum(numbers, target):
  for x in numbers:
    for y in numbers:
      if x+y == target:
        return True
  return False

def first_invalid(numbers, preamble):
  buffer = numbers[:preamble+1]
  for n in numbers[preamble+1:]:
    buffer = buffer[1:]
    buffer.append(n)
    if not is_sum(buffer, n):
      return n
  return None

def part_2(numbers, target):
  start, end = 0, 1
  while start < len(numbers) and end < len(numbers):
    if sum(numbers[start:end]) < target:
      end = end + 1
    while sum(numbers[start:end]) > target:
      start = start + 1
    if sum(numbers[start:end]) == target:
      return numbers[start:end]
  return None

lines = [int(l) for l in lines]
target = first_invalid(lines, 25)
print('Part 1:', target)

res = part_2(lines, target)
print('Part 2:', max(res)+min(res))

print()