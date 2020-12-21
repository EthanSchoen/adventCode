lines = open('days/day17_input.txt', "r").read().split('\n')
# lines = open('test.txt', "r").read().split('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 17 ~~~~~~~~~~~~~~~~~~~~~~~~~')

def num_near(m, x, y, z):
  count = 0
  for i in range(x-1,x+2):
    for j in range(y-1,y+2):
      for k in range(z-1,z+2):
        if i == x and j == y and k == z:
          continue
        if (0 <= i < len(m)) and (0 <= j < len(m[0])) and (0 <= k < len(m[0][0])):
          if m[i][j][k] == '#':
            count = count + 1
  return count

def m_increase(m):
  n = []
  for x in range(-1, len(m)+1):
    n.append([])
    for y in range(-1, len(m[0])+1):
      n[x+1].append([])
      for z in range(-1, len(m[0][0])+1):
        n[x+1][y+1].append(m[x][y][z] if 0<=x<len(m) and 0<=y<len(m[0]) and 0<=z<len(m[0][0]) else '.')
  return n

def pmat(m):
  for z in range(len(m[0][0])):
    print('z:', z - (len(m[0][0])//2))
    for x in range(len(m)):
      for y in range(len(m[0])):
        print(m[x][y][z], end='')
      print(end='\t')
      for y in range(len(m[0])):
        print(num_near(m, x, y, z), end='')
      print()

matrix = [[[lines[x][y]] for y in range(len(lines))] for x in range(len(lines[0]))]
matrix = m_increase(matrix)
count = 0
for _ in range(6):
  count = 0
  increase = False
  newm = []
  for x in range(len(matrix)):
    newm.append([])
    for y in range(len(matrix[0])):
      newm[x].append([])
      for z in range(len(matrix[0][0])):
        near = num_near(matrix, x, y, z)
        if matrix[x][y][z] == '#':
          newm[x][y].append('#' if (1 < near < 4) else '.')
        else:
          if near == 3:
            newm[x][y].append('#')
            if x==0 or x==(len(matrix)-1) or y==0 or y==(len(matrix[0])-1) or z==0 or z==(len(matrix[0][0])-1):
              increase = True
          else:
            newm[x][y].append('.')
        if newm[x][y][z] == '#':
          count = count + 1
  matrix = m_increase(newm) if increase else newm
print('Part 1:', count)


def num_near(m, x, y, z, w):
  count = 0
  for i in range(x-1,x+2):
    for j in range(y-1,y+2):
      for k in range(z-1,z+2):
        for l in range(w-1,w+2):
          if i == x and j == y and k == z and l == w:
            continue
          if (0 <= i < len(m)) and (0 <= j < len(m[0])) and (0 <= k < len(m[0][0])) and (0 <= l < len(m[0][0][0])):
            if m[i][j][k][l] == '#':
              count = count + 1
  return count

def m_increase(m):
  n = []
  for x in range(-1, len(m)+1):
    n.append([])
    for y in range(-1, len(m[0])+1):
      n[x+1].append([])
      for z in range(-1, len(m[0][0])+1):
        n[x+1][y+1].append([])
        for w in range(-1, len(m[0][0][0])+1):
          n[x+1][y+1][z+1].append(m[x][y][z][w] if 0<=x<len(m) and 0<=y<len(m[0]) and 0<=z<len(m[0][0]) and 0<=w<len(m[0][0][0]) else '.')
  return n

# def pmat(m):
#   for z in range(len(m[0][0])):
#     print('z:', z - (len(m[0][0])//2))
#     for x in range(len(m)):
#       for y in range(len(m[0])):
#         print(m[x][y][z], end='')
#       print(end='\t')
#       for y in range(len(m[0])):
#         print(num_near(m, x, y, z), end='')
#       print()

matrix = [[[[lines[x][y]]] for y in range(len(lines))] for x in range(len(lines[0]))]
matrix = m_increase(matrix)
count = 0
for _ in range(6):
  count = 0
  increase = False
  newm = []
  for x in range(len(matrix)):
    newm.append([])
    for y in range(len(matrix[0])):
      newm[x].append([])
      for z in range(len(matrix[0][0])):
        newm[x][y].append([])
        for w in range(len(matrix[0][0][0])):
          near = num_near(matrix, x, y, z, w)
          if matrix[x][y][z][w] == '#':
            newm[x][y][z].append('#' if (1 < near < 4) else '.')
          else:
            if near == 3:
              newm[x][y][z].append('#')
              if x==0 or x==(len(matrix)-1) or y==0 or y==(len(matrix[0])-1) or z==0 or z==(len(matrix[0][0])-1) or w==0 or w==(len(matrix[0][0][0])-1):
                increase = True
            else:
              newm[x][y][z].append('.')
          if newm[x][y][z][w] == '#':
            count = count + 1
  matrix = m_increase(newm) if increase else newm
print('Part 2:', count)

print()