lines = open('days/day14_input.txt', "r").read().split('\n')
# lines = open('test.txt', "r").read().split('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 14 ~~~~~~~~~~~~~~~~~~~~~~~~~')

mask = ''
mem = {}
for ins in lines:
  if ins[:4] == 'mask':
    mask = ins[:6:-1]
    continue
  add = ins[ins.index('[')+1:ins.index(']')]
  binary = str(bin(int(ins[ins.index('=')+2:])))[:1:-1]
  for i in range(len(mask)):
    if i >= len(binary):
      binary = binary + ('0' if mask[i] == 'X' else mask[i])
      continue
    if mask[i] == 'X':
      continue
    if mask[i] == '0':
      binary = binary[:i] +'0' + binary[i+1:]
    if mask[i] == '1':
      binary = binary[:i] +'1' + binary[i+1:]
  binary = binary[::-1]
  mem[add] = int(binary, 2)
print('Part 1:', sum(mem.values()))

def place_in_mem(mem, add, val):
  x = add.find('X')
  if x == -1:
    mem[str(int(add,2))] = val
    return mem
  return place_in_mem(mem, add[:x]+'0'+add[x+1:], val) | place_in_mem(mem, add[:x]+'1'+add[x+1:], val)
mem = {}
for ins in lines:
  if ins[:4] == 'mask':
    mask = ins[:6:-1]
    continue
  add = str(bin(int(ins[ins.index('[')+1:ins.index(']')])))[:1:-1]
  value = int(ins[ins.index('=')+2:])
  for i in range(len(mask)):
    if i >= len(add):
      add = add + mask[i:]
      break
    if mask[i] == '0':
      continue
    if mask[i] == '1':
      add = add[:i] +'1' + add[i+1:]
    if mask[i] == 'X':
      add = add[:i] +'X' + add[i+1:]
  add = add[::-1]
  mem = place_in_mem(mem, add, value)
print('Part 2:', sum(mem.values()))

print()