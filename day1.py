numbers = open('day1_input.txt', "r").read().split('\n')
numbers = list(map(int, numbers))

# Part 1
def part1():
  res = -1
  for n in numbers:
    other = 2020-n
    for o in numbers:
      if o == other:
        res = o * n
        print(f'Part 1 Result: {n} * {o} = {res}')
        return

# Part 2
def part2():
  res = -1
  for n in numbers:
    other1 = 2020-n
    for o1 in numbers:
      if o1 < other1:
        other2 = 2020-n-o1
        for o2 in numbers:
          if o2 == other2:
            res = n * o1 * o2
            print(f'Part 2 Result: {n} * {o1} * {o2} = {res}')
            return

part1()
print()
part2()