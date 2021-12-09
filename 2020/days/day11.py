grid = open('days/day11_input.txt', "r").read().split('\n')
# grid = open('test.txt', "r").read().split('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 11 ~~~~~~~~~~~~~~~~~~~~~~~~~')

def count_adjacent(grid, x, y):
  count = 0
  for i in range(x-1,x+2):
    for j in range(y-1,y+2):
      if i == x and j == y:
        continue
      if 0 <= i < len(grid[0]) and 0 <= j < len(grid):
        if grid[j][i] == '#':
          count = count + 1
  return count

def count_visible(grid, x, y):
  count = 0
  directions = [(-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0)]
  for d in directions:
    i, j = x+d[0], y+d[1]
    while True:
      if 0 <= i < len(grid[0]) and 0 <= j < len(grid):
        if grid[j][i] == '#':
          count = count + 1
          break
        if grid[j][i] == 'L':
          break
      else:
        break
      i, j = i+d[0], j+d[1]
  return count

def occupied(grid):
  count = 0
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == '#':
        count = count + 1
  return count

def print_grid(grid):
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      print(grid[y][x], end='')
    print()

def part1(grid):
  while True:
    next_grid = []
    for y in range(len(grid)):
      next_grid.append('')
      for x in range(len(grid[0])):
        if grid[y][x] == '.':
          next_grid[y] = next_grid[y] + '.'
        if grid[y][x] == '#':
          if count_adjacent(grid, x, y) >= 4:
            next_grid[y] = next_grid[y] + 'L'
          else:
            next_grid[y] = next_grid[y] + '#'
        if grid[y][x] == 'L':
          if count_adjacent(grid, x, y) == 0:
            next_grid[y] = next_grid[y] + '#'
          else:
            next_grid[y] = next_grid[y] + 'L'
    if next_grid == grid:
      break
    grid = next_grid
  return occupied(grid)
print('Part 1:', part1(grid))

def part2(grid) :
  while True:
    next_grid = []
    for y in range(len(grid)):
      next_grid.append('')
      for x in range(len(grid[0])):
        if grid[y][x] == '.':
          next_grid[y] = next_grid[y] + '.'
        if grid[y][x] == '#':
          if count_visible(grid, x, y) >= 5:
            next_grid[y] = next_grid[y] + 'L'
          else:
            next_grid[y] = next_grid[y] + '#'
        if grid[y][x] == 'L':
          if count_visible(grid, x, y) == 0:
            next_grid[y] = next_grid[y] + '#'
          else:
            next_grid[y] = next_grid[y] + 'L'
    if next_grid == grid:
      break
    grid = next_grid
  return occupied(grid)
print('Part 2:', part2(grid))

print()