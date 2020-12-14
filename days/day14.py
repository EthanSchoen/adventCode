lines = open('days/day14_input.txt', "r").read().split('\n')
# lines = open('test.txt', "r").read().split('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 14 ~~~~~~~~~~~~~~~~~~~~~~~~~')

mask = lines[0][:6:-1]
print(mask)
mem = {}
for ins in lines[1:]:
  add = ins[4]
  binary = str(bin(int(ins[9:])))[:1:-1]
  for i in range(len(binary)):
    if mask[i] == 'X':
      continue
    if mask[i] == '0':
      print(binary)
      binary = binary[:i] +'0' + binary[i+1:]
      print(binary)
    if mask[i] == '1':
      # binary[i] = '1'
      binary = binary[:i] +'1' + binary[i+1:]
  binary = binary[::-1]
  mem[add] = int(binary, 2)
print('Part 1:', sum(mem.values()))

print()