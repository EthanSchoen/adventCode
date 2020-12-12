lines = open('days/day12_input.txt', "r").read().split('\n')
# lines = open('test.txt', "r").read().split('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 12 ~~~~~~~~~~~~~~~~~~~~~~~~~')

ns = 0
ew = 0
facing = 1
dirs = {0:'N', 1:'E', 2:'S', 3:'W'}
for i in lines:
  t = i[0]
  val = int(i[1:])
  if t == 'F':
    t = dirs[facing]
  if t == 'L':
    facing = (facing + 4 - val//90)%4
  if t == 'R':
    facing = (facing + val//90)%4

  if t == 'N':
    ns = ns + val
  if t == 'E':
    ew = ew + val
  if t == 'S':
    ns = ns - val
  if t == 'W':
    ew = ew - val
print('Part 1:', abs(ns)+abs(ew))

def rotate(x, y, amt):
  if amt == 1:
    return [y, -x]
  if amt == 2:
    return [-x, -y]
  if amt == 3:
    return [-y, x]

ns = 1
ew = 10
pos = [0, 0]
for i in lines:
  t = i[0]
  val = int(i[1:])
  if t == 'F':
    pos[0], pos[1] = pos[0] + ns*val, pos[1] + ew*val
  if t == 'L':
    res = rotate(ns, ew, (val//90)%4)
    ns, ew = res[0], res[1]
  if t == 'R':
    res = rotate(ns, ew, (4 - val//90)%4)
    ns, ew = res[0], res[1]

  if t == 'N':
    ns = ns + val
  if t == 'E':
    ew = ew + val
  if t == 'S':
    ns = ns - val
  if t == 'W':
    ew = ew - val
print('Part 2:', abs(pos[0])+abs(pos[1]))

print()