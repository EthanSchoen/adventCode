lines = open('days/day3_input.txt', "r").read().split('\n')

print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 3 ~~~~~~~~~~~~~~~~~~~~~~~~~')

def check_slope(angle, lines, down):
  x = angle
  trees = 0
  width = len(lines[0])
  for l in lines[down::down]:
    if (l[x] == '#'):
      trees = trees + 1
    x = (x + angle) % width
  return trees

print(check_slope(1, lines, 1) * check_slope(3, lines, 1) * check_slope(5, lines, 1) * check_slope(7, lines, 1) * check_slope(1, lines, 2))
print()