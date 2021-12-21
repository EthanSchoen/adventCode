
input = open('days/day04_input.txt', "r").read().split('\n')
numbers = input[0].split(',')
input = input[1:]
boards = []
for l in range(int(len(input)/6)):
  s, e = l*6+1, l*6+6
  boards.append(list(map(lambda l: l.split(), input[s:e])))

print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 4 ~~~~~~~~~~~~~~~~~~~~~~~~~')

def checkForWin(board):
  # rows
  for l in board:
    marked = []
    for c in l:
      if c[0] == 'x':
        marked.append(c[1:])
    if len(marked) == 5:
      return marked
  # columns
  for i in range(5):
    marked = []
    for j in range(5):
      if board[j][i][0] == 'x':
        marked.append(board[j][i][1:])
    if len(marked) == 5:
      return marked
  return []

# Part 1
def part1():
  for n in numbers:
    for b in boards:
      for l in b:
        for c in range(len(l)):
          if l[c] == n:
            l[c] = 'x' + l[c]
      res = checkForWin(b)
      if (len(res) > 0):
        unmarked = []
        for l in b:
          for c in l:
            if c[0] != 'x':
              unmarked.append(int(c))
        return sum(unmarked)*int(n)
  return

# Part 2
def part2():
  for n in numbers:
    remove = []
    for i in range(len(boards)):
      b = boards[i]
      for l in b:
        for c in range(len(l)):
          if l[c] == n:
            l[c] = 'x' + l[c]
      res = checkForWin(b)
      if (len(res) > 0):
        if len(boards) == 1:
          unmarked = []
          for l in boards[0]:
            for c in l:
              if c[0] != 'x':
                unmarked.append(int(c))
          return sum(unmarked)*int(n)
        remove.append(i)
    if len(remove):
      offset = 0
      while len(remove) and len(boards) > 1:
        del boards[remove.pop(0) - offset]
        offset += 1
  return

print('part1: ' + str(part1()))
print('part2: ' + str(part2()))
print()
